# 🎓 Django Student Management System

A sleek, **user-friendly** Student Management System built with **Django**.  
Designed for educational institutions to manage students, courses, revenue, settings, and send **PDF receipts via email**.  


---

## 🚀 Features & Live Demo

| Feature | Description | Demo |
|---------|-------------|------|
| 🏠 **Dashboard** | Overview of students, courses, and revenue. | [Live Demo](#) |
| 👩‍🎓 **Student Management** | Add, view, update, and delete students. | [Live Demo](#) |
| 📚 **Course Management** | Manage courses and enrollments. | [Live Demo](#) |
| 💰 **Revenue Tracking** | Interactive monthly revenue charts. | [Live Demo](#) |
| ⚙️ **Settings** | Securely update app configurations. | [Live Demo](#) |
| 🔒 **Logout** | End session securely. | [Live Demo](#) |
| 📨 **PDF Receipt Email** | Send PDF receipts after registration. | [Live Demo](#) |

---

## 🛠️ Tech Stack & Badges

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![SQLite](https://img.shields.io/badge/database-SQLite-orange)
![Chart.js](https://img.shields.io/badge/charts-Chart.js-red)
![PDF](https://img.shields.io/badge/PDF-WeasyPrint-yellow)
![Email](https://img.shields.io/badge/email-SMTP-lightgrey)

---

## 📍 URL Paths / Views

| Path | View | Description |
|------|------|-------------|
| `/` | 🏠 Dashboard | Overview of students, courses, and revenue. |
| `/students/` | 👩‍🎓 Students | Add, view, and manage students. |
| `/courses/` | 📚 Courses | Manage courses and enrollments. |
| `/revenue/` | 💰 Revenue | Interactive charts for revenue tracking. |
| `/settings/` | ⚙️ Settings | Update app configurations securely. |
| `/logout/` | 🔒 Logout | End your session securely. |

---

## 📸 Screenshots
**🏠 Dashboard:**  
![Dashboard Screenshot](assets/dashboard.png)  

**👩‍🎓 Student Management:**  
![Students Screenshot](assets/Student-registration-form.png)  

**📚 Course Overview:**  
![Courses Screenshot](assets/course-overview.png)  

**💰 Revenue Analytics:**  
![Revenue Screenshot](assets/revenue-analytics.png)  

**⚙️ Settings Page:**  
![Settings Screenshot](assets/Settings-page.png)  

**🔒 Logout Page:**  
![Logout Screenshot](assets/logout-page.png)  

**📝 PDF Receipt via Email:**  
![PDF Receipt Screenshot](assets/receipt.png)  


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
│   │   ├── dashboard.html
│   │   ├── students.html
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
