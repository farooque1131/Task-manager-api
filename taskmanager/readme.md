- Task Manager REST API

A clean and powerful Task Management API built using Django, Django REST Framework, JWT Authentication, Role-based Permissions, and Django Filters.

This backend project is designed in a professional way suitable for internships, job interviews, production learning, and real-world applications.

- Features
- Authentication

User registration

JWT login (access + refresh token)

Token refresh

Admin role support

Secure password validation

User Management (Admin Only)

List all registered users

Promote/demote users (update is_staff)

- Task Management

Create tasks

List all tasks

Retrieve a specific task

Update/Delete tasks

Only admin and task owner can edit/delete

Everyone can view tasks

- Search & Filtering (via django-filter)

Search by title or description

Filter by owner ID

Filter by status

Sort by creation date

- Technology Stack

Python 3.x

Django 5

Django REST Framework

Simple JWT Authentication

Django Filter

SQLite (Default)

📁 Installation & Setup
1. Clone the Repository
git clone https://github.com/farooque1131/Task-manager-api.git
cd <your-repo>

2. Create Virtual Environment
python -m venv env
source env/bin/activate   # Linux / Mac
env\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
pthon manage.py makemigrations
python manage.py migrate

6. Run Server
python manage.py runserver

- API Endpoints Documentation

Below is a clean summary of all available API endpoints.

1. Authentication Endpoints
Register User
POST /api/auth/register/

Login (JWT Access + Refresh)
POST /api/auth/login/

Refresh Token
POST /api/auth/refresh/

2. User Management (Admin Only)
List All Users
GET /api/auth/users/

Update User Role (Promote/Demote Staff)
PATCH /api/auth/users/update-role/<id>/

3. Task Endpoints
List / Create Tasks
GET  /api/tasks/add/
POST /api/tasks/add/

Retrieve / Update / Delete Task
GET    /api/tasks/retrive/<id>
PUT    /api/tasks/retrive/<id>
PATCH  /api/tasks/retrive/<id>
DELETE /api/tasks/retrive/<id>


📂 Project Structure (Simple Overview)
project/
│── users/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│── tasks/
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│── settings.py
│── requirements.txt
│── README.md

Author

Farooque Shaikh
