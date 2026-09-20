Habit Tracker

A simple web-based habit tracking application built with Django.

Habit Tracker allows users to create and manage their daily habits, track their completion history, and monitor their progress through a simple dashboard.

This project was built as a practical Django project to review and apply core concepts such as models, relationships, authentication, forms, CRUD operations, Django ORM, templates, and user-specific data management.

---

Features

- User registration and authentication
- Create, edit, and delete habits
- Activate and deactivate habits
- Track habit completion
- View habit completion history
- Dashboard with habit statistics
- Current streak tracking
- User-specific habit data
- Form validation
- Success and error messages
- Responsive and simple UI

---

Tech Stack

- Python
- Django
- PostgreSQL
- HTML
- CSS


---


Data Models

The application uses two main models in addition to Django's built-in "User" model.

User

Django's built-in authentication model is used to manage users and authentication.

Habit

Represents a habit created by a user.

Main fields:

- "user"
- "name"
- "description"
- "is_active"
- "created_at"
- "updated_at"

Relationship:

User 1 ───────── N Habit

HabitLog

Stores the completion history of a habit.

Main fields:

- "habit"
- "date"
- "date"

Relationship:

Habit 1 ───────── N HabitLog

Each habit can have only one completion log for a specific date.

---

Main Pages


Authentication

- Register
- Login
- Logout

Dashboard

Provides an overview of the user's habits and progress, including:

- Active habits
- Completed habits
z- Current streaks
- Today's habit status

Habit List

Displays the user's habits and provides access to habit management actions.

Create Habit

Allows users to create a new habit.

Edit Habit

Allows users to modify an existing habit.

Habit Detail

Displays detailed information and completion history for a specific habit.

Delete Habit

Allows users to permanently remove a habit.

---

Security and User Data

Each user's habits are isolated from other users.

Users can only:

- View their own habits
- Edit their own habits
- Delete their own habits
- Create completion logs for their own habits

Authentication-protected views require the user to be logged in.

---

Installation

1. Clone the repository

git clone https://github.com/SkillMoon/Habit-Tracker
cd habit-tracker

2. Create a virtual environment

Windows:

python -m venv venv

Linux / macOS:

python3 -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Apply migrations

python manage.py migrate

6. Create a superuser

python manage.py createsuperuser

7. Run the development server

python manage.py runserver

Open the application at:

http://127.0.0.1:8000/

---

Django Admin

The project includes Django Admin for managing users, habits, and habit logs.

After creating a superuser, access the admin panel at:

http://127.0.0.1:8000/admin/

---

What I Practiced

This project was created to reinforce the following Django concepts:

- Django project and app structure
- Models and model relationships
- ForeignKey
- Model constraints
- Migrations
- Django ORM and QuerySets
- CRUD operations
- ModelForms
- Form validation
- Django authentication
- Login and logout
- "request.user"
- Access control and user-specific queries
- Templates and template inheritance
- Static files
- URL routing
- Custom business logic
- Streak calculation
- Django Admin

---

