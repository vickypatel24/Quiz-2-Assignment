# Employee Analytics API

A Django + Django REST Framework based web application that:

- Generates synthetic employee data
- Stores data in SQLite (default Django database)
- Provides REST API endpoints for data retrieval and analytics
- Visualizes data using Chart.js (optional frontend) or Swagger UI
- Implements API rate limiting using Django REST Framework throttling

---

## 🚀 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default database)
- drf-yasg (for Swagger documentation)
- Faker (for synthetic data generation)
- Chart (for frontend data visualization)

---

## 📦 Features

- Employee data model
- API to list all employees
- API to retrieve employee analytics (average salary, max/min salary, total employees)
- Swagger UI for interactive API exploration
- SQLite integration
- Command to generate 100+ fake employees
- Rate limiting on API endpoints
- Visualize employee salary distribution using Chart
---

## 🛠 Installation Guide

1. **Clone the Repository**

git clone https://github.com/vickypatel24/Quiz-2-Assignment.git
cd employee-analytics

Create a Virtual Environment
-python -m venv venv
-source venv/bin/activate    # Windows: venv\Scripts\activate

Install Dependencies
-pip install -r requirements.txt

Apply Migrations
-python manage.py makemigrations
-python manage.py migrate

Generate Synthetic Employee Data
-python manage.py generate_employees

Run Development Server
-python manage.py runserver

### Access your application
URL:- http://127.0.0.1:8000/

Access Swagger API docs at
URL:- http://127.0.0.1:8000/swagger/

Show Employee chart
URL:- http://127.0.0.1:8000/api/chart/

Download CSV
URL:- http://127.0.0.1:8000/api/export/csv/


