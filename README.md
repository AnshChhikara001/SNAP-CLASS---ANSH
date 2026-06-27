# 🎓 SnapClass

> **An AI-powered Attendance Management System built with Streamlit, Face Recognition, Voice Recognition, and Supabase.**

SnapClass is a smart attendance management system that simplifies classroom attendance using AI. It provides dedicated portals for teachers and students, allowing attendance to be marked through facial and voice verification while keeping attendance records organized in the cloud.

---

## ✨ Features

### 👨‍🏫 Teacher Portal

* Secure Login & Registration
* Create and Manage Subjects
* View Attendance Records
* Share Subjects using QR Code, Join Link, or Subject Code
* Manage Student Enrollments

### 👨‍🎓 Student Portal

* Secure Login
* Join Subjects
* Face Recognition Attendance
* Voice Verification
* View Enrolled Subjects
* Track Attendance History

### 🤖 AI Features

* Face Recognition
* Voice Recognition
* Automatic Attendance Marking
* Secure Identity Verification

---

## 🛠 Tech Stack

| Category         | Technologies                                      |
| ---------------- | ------------------------------------------------- |
| Frontend         | Streamlit                                         |
| Database         | Supabase                                          |
| AI               | face_recognition, dlib, Resemblyzer, scikit-learn |
| Audio            | librosa, soundfile, scipy                         |
| QR Code          | segno                                             |
| Image Processing | Pillow                                            |
| Security         | bcrypt                                            |
| Utilities        | NumPy, Pandas                                     |

---

## 📁 Project Structure

```
SNAP-CLASS
│
├── src
│   ├── components
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_records.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendence.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
│   ├── database
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── pipelines
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── screens
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   └── ui
│       └── base_layout.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/AnshChhikara001/SNAP-CLASS---ANSH.git

cd SNAP-CLASS---ANSH
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Teacher creates a subject.
2. Students join using a QR Code, Join Link, or Subject Code.
3. The system verifies the student's identity using Face Recognition and Voice Recognition.
4. Attendance is automatically stored in Supabase.
5. Teachers can monitor attendance records in real time.

---

## 📚 Libraries Used

* Streamlit
* NumPy
* Pandas
* scikit-learn
* dlib
* face_recognition
* Supabase
* bcrypt
* segno
* Pillow
* librosa
* Resemblyzer
* soundfile
* scipy

---

## 🚀 Future Improvements

* Liveness Detection
* Anti-Spoofing
* Attendance Analytics
* Mobile Application
* Email Notifications
* Admin Dashboard
* Multi-Face Recognition

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve SnapClass, feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub.

---

## 👨‍💻 Author

**Ansh Chhikara**

GitHub: **https://github.com/AnshChhikara001**
