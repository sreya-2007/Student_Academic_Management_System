# 🎓 Student Productivity & Academic Management System

> A beginner-friendly web-based application designed to help students manage and organize their academic activities in one centralized platform.

## 📌 Project Overview

Students often need to keep track of multiple academic details such as subjects, attendance, assignments, deadlines, and examination marks.

The **Student Productivity & Academic Management System** provides a simple and centralized platform where students can efficiently organize, monitor, and manage their academic records from a single dashboard.

## 🎯 Objectives

* 📚 Manage student subjects and course information
* 📈 Track attendance and calculate attendance percentage
* 📅 Manage assignments and their deadlines
* 📝 Record examination and assessment marks
* 📊 Provide a centralized academic dashboard
* 🗄️ Store academic information using a database

## ✨ Features

### 📊 Dashboard

Provides an overview of:

* Total subjects
* Overall attendance
* Assignments
* Recent marks

### 📚 Subject Management

Students can:

* Add subjects
* Store course codes
* Store teacher information
* Delete subjects

### 📈 Attendance Management

Students can:

* Enter total classes
* Enter attended classes
* Automatically calculate attendance percentage
* View attendance records

### 📅 Assignment Management

Students can:

* Add assignments
* Add subject information
* Set assignment deadlines
* Mark assignments as completed
* Delete assignments

### 📝 Marks Management

Students can:

* Record examination and assessment marks
* Store total marks
* Calculate percentages
* View marks records
* Delete records

## 🛠️ Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| HTML       | Application Structure  |
| CSS        | Styling and UI Design  |
| JavaScript | Frontend Interactivity |
| Python     | Backend Programming    |
| Flask      | Web Framework          |
| SQLite     | Database Management    |

## 🏗️ Project Architecture

```text
User
  ↓
Web Interface
  ↓
HTML / CSS / JavaScript
  ↓
Python Flask Backend
  ↓
SQLite Database
  ↓
Academic Records
```

## 🗄️ Database

The application uses **SQLite** to store and manage academic information.

The database contains tables for:

* 📚 Subjects
* 📈 Attendance
* 📅 Assignments
* 📝 Marks

> The database is automatically created when the application is started.

## 📂 Application Modules

| Module                | Description                                 |
| --------------------- | ------------------------------------------- |
| 📊 Dashboard          | Provides an overview of academic activities |
| 📚 Subject Management | Add and manage subjects                     |
| 📈 Attendance Tracker | Track classes and attendance percentage     |
| 📅 Assignment Tracker | Manage assignments and deadlines            |
| 📝 Marks Tracker      | Record and monitor examination marks        |

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Student-Academic-Management-System
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

#### Windows PowerShell

```bash
venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Application

```bash
python app.py
```

### 7️⃣ Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔮 Future Improvements

The project can be further enhanced with:

* 🔐 Student login and authentication
* 👥 Multiple student accounts
* 🗄️ MySQL database support
* 📊 Graphical academic performance analysis
* 🔔 Assignment reminders
* 📧 Email notifications
* 📱 Mobile-friendly UI improvements
* 🤖 Academic performance analytics

## 👩‍💻 Developer

**Sreya M**

Bachelor of Technology in Computer Science and Engineering

Lovely Professional University

## 📄 License

This project is created for **educational and academic purposes**.

---

⭐ **If you found this project useful, consider giving it a star!**
