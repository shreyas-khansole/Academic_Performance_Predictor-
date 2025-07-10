# 🎓 Academic Performance Predictor 🚀  
*A smart student assistant that predicts your grade, pass/fail status, and builds a personalized weekly study timetable!*

![App Preview](https://img.shields.io/badge/Made%20with-Flask-ff0000?style=for-the-badge&logo=flask)
![ML-Powered](https://img.shields.io/badge/Machine%20Learning-Yes-brightgreen?style=for-the-badge&logo=scikit-learn)
![Stars](https://img.shields.io/github/stars/yourusername/academic-predictor?style=for-the-badge)
![License](https://img.shields.io/github/license/yourusername/academic-predictor?style=for-the-badge)

---

## 🔮 What It Does

✨ This AI-powered app takes in your subject marks, study habits, distractions, and sleep, and gives you:

- ✅ **Pass or Fail Prediction**
- 🅰️ **Grade Prediction** (A/B/C/D/F)
- 🗓️ **Personalized Study Timetable**
- 📚 **Recommended Books for Weak Subjects**
- ⚠️ **Feedback on Distraction & Sleep**

> Built with 🔥 Flask + Scikit-Learn + Love + Late Night Debugging.

---

## 🧠 Behind the Scenes

### 🏗️ Tech Stack
- **Frontend**: HTML, CSS (Bootstrap-like clean style)
- **Backend**: Flask (Python)
- **ML Models**: Decision Tree Classifier
- **Data**: `Student_performance_10k.csv` (Custom dataset with 10,000 rows!)

### 📦 Models Used
- `grade_model.pkl`: Predicts your grade.
- `pass_model.pkl`: Predicts pass/fail.
- `le_grade.pkl` & `le_pass.pkl`: Label encoders.
- Stored inside `/models` folder.

---

## 🚀 How to Run It

1. **Clone This Repo**
   ```bash
   git clone https://github.com/yourusername/academic-predictor.git
   cd academic-predictor
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**
   ```bash
   python app.py
   ```

4. **Go to Browser**
   Open `http://127.0.0.1:5000` to use the app!

---

## ✍️ Sample Inputs

| Subject     | Marks |
|-------------|-------|
| English     | 78    |
| Maths       | 65    |
| Science     | 55    |
| SST         | 40    |
| Hindi       | 82    |
| GK          | 30    |

Also enter:
- 📘 Study Hours/day: `2.5`
- 🎯 Distraction Time/day: `4.0`
- 😴 Sleep Hours/day: `5.5`

> 💥 Get instant results + timetable + book tips + motivational warnings if needed!

---

## 📸 Screenshots

### 🖥️ Home Page (Form)
> *User-friendly interface to enter subject marks and habits*

![homepage](https://github.com/user-attachments/assets/0dcaac5f-966c-40cc-8c29-5e8d3b825ec2)


---

### 📊 Result Page
> *Timetable, book tips & personalized feedback*

  ![predicton for less marks](https://github.com/user-attachments/assets/2440efc2-e05d-4243-a151-820a522f3a44)


---

## 📚 Book Suggestions

| Subject | Recommended Book |
|---------|------------------|
| English | Wren & Martin     |
| Maths   | RD Sharma         |
| Science | Lakhmir Singh     |
| SST     | NCERT SST         |
| Hindi   | NCERT Hindi       |
| GK      | Lucent GK         |

---

## 🧠 Future Ideas

- 🧑‍🎓 Login system with progress tracking  
- 📈 Weekly performance dashboard  
- 📤 Export to PDF  
- 🧩 Adaptive learning tips  

---

## 🤝 Contribute

Pull requests are welcome! If you find bugs or want new features, create an issue or PR.

---

## 💼 Author

Made with ❤️ by **[Shreyas Khansole](https://github.com/shreyas-khansole)**  
Drop a ⭐ if this helped!

---

## 📜 License

MIT License
