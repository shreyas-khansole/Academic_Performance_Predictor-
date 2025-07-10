from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load models from the 'models' folder
grade_model = joblib.load("models/grade_model.pkl")
pass_model = joblib.load("models/pass_model.pkl")
le_grade = joblib.load("models/le_grade.pkl")
le_pass = joblib.load("models/le_pass.pkl")

subjects = ["English", "Maths", "Science", "SST", "Hindi", "GK"]

book_suggestions = {
    "English": "Wren & Martin",
    "Maths": "RD Sharma",
    "Science": "Lakhmir Singh",
    "SST": "NCERT SST",
    "Hindi": "NCERT Hindi",
    "GK": "Lucent GK"
}

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")  # Show the input form

@app.route("/predict", methods=["POST"])
def predict():
    try:
        marks = [int(request.form[s]) for s in subjects]
        study_hours = float(request.form['study_hours'])
        distraction = float(request.form['distraction_time'])
        sleep = float(request.form['sleep_time'])

        input_data = np.array(marks + [study_hours, distraction, sleep]).reshape(1, -1)

        pass_pred = le_pass.inverse_transform(pass_model.predict(input_data))[0]
        grade_pred = le_grade.inverse_transform(grade_model.predict(input_data))[0]

        weak_subjects = [sub for i, sub in enumerate(subjects) if marks[i] < 40]
        recommended_books = [book_suggestions[sub] for sub in weak_subjects]

        # Weekly timetable
        timetable = []
        slots = ["4–6 PM", "7–9 PM"]
        week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        study_plan = weak_subjects if grade_pred in ['D', 'F'] else subjects

        for i in range(7):
            day = week_days[i]
            s1 = study_plan[i % len(study_plan)]
            s2 = study_plan[(i + 1) % len(study_plan)]
            timetable.append({"day": day, "slot1": s1, "slot2": s2})

        feedback = []
        if distraction > 3:
            feedback.append("⚠️ High distraction time. Try to reduce it.")
        if sleep < 6:
            feedback.append("😴 Low sleep time. Try to sleep more.")

        return render_template("result.html",
            pass_result=pass_pred,
            grade_result=grade_pred,
            timetable=timetable,
            recommended_books=recommended_books,
            feedback=feedback
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
