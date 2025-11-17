🎓 Paritie Student Management System

A sleek, user-friendly Student Management System built with Django.
Designed for Paritie Innovation Hub to manage students, co-workers (members), courses, revenue, settings, and send PDF receipts via email.

🚀 Features
Feature	Description
🏠 Dashboard	Overview of students, members, courses, and revenue.
👩‍🎓 Student Management	Add, view, update, and delete students.
🧑‍💼 Member Management	Manage co-workers and their membership plans.
📚 Course Management	Add, view, and manage courses and enrollments.
💰 Revenue Tracking	Interactive monthly revenue charts for students and members.
⚙️ Settings	Securely update app configurations.
🔒 Logout	End session securely.
📨 PDF Receipt Email	Automatically send PDF receipts after registration.
---

## 🛠️ Tech Stack & Badges

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![Database: MySQL (hosted on Aiven Cloud)](https://img.shields.io/badge/database-SQLite-orange)
![Chart.js](https://img.shields.io/badge/charts-Chart.js-red)
![PDF](https://img.shields.io/badge/PDF-WeasyPrint-yellow)
![Email](https://img.shields.io/badge/email-SMTP-lightgrey)

---

## 📍 URL Paths / Views

| Path | View | Description |
|------|------|-------------|
| `/` |Login page, available only for registered users in the admin|
| `/` | 🏠 Dashboard | Overview of students, courses, and revenue. |
| `/students/` | 👩‍🎓 Students | Add, view, and manage students. |
| `/members/` | 👩‍🎓 Members | Add, view, and manage members. |
| `/courses/` | 📚 Courses | Manage courses and enrollments. |
| `/revenue/` | 💰 Revenue | Interactive charts for revenue tracking. |
| `/settings/` | ⚙️ Settings | Update app configurations securely. |
| `/logout/` | 🔒 Logout | End your session securely and back to login page. |

---


---

## ⚡ Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

🔧 Environment Variables

Create a .env file:
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password


🎯 Future Enhancements

Role-based access: admin, teacher, student

Cloud database integration (AWS RDS/PostgreSQL)

Exportable reports (PDF/Excel)

Advanced filtering & search

Templated email receipts

👨‍💻 Author
Fadilah Abdulkadir
Site Reliability Engineer | Backend Developer | AWS Cloud Solutions Architect
Aspiring Full-Stack Developer | Django Enthusiast | Python Avid

💎 Why This Project Stands Out

Clean Architecture: Easy to maintain and extend

Interactive Charts: Quick visual insights

PDF Receipts: Professional email receipts for students

 Full-stack Django, UI, email, and database showcase

   Project Structure
student_management_system/
├── manage.py
├── student_app/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── students.html
│   │   ├── members.html
│   │   ├── courses.html
│   │   ├── revenue.html
│   │   ├── settings.html
│   │   └── logout.html
│   └── static/
├── db.sqlite3
├── requirements.txt
└── .env



# Run the server
python manage.py runserver
