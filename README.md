# Learning Platform

A full-stack web application that allows students to discover, enroll in, and track online courses while providing administrators with course management capabilities.

---

## Overview

Learning Platform is an online course management system designed to connect students with educational content. Students can browse courses, enroll in them, track their learning progress, and leave reviews. Administrators can manage courses and monitor enrollments through a dedicated administration panel.

---

## Features

### Student Features

* Register and log in securely.
* Browse available courses.
* Filter courses based on preferences.
* View detailed course information.
* Enroll in courses.
* Track learning progress.
* Create custom course lists.
* Rate and review enrolled courses.

### Admin Features

* Add new courses.
* Update existing course information.
* Delete courses.
* View students enrolled in a course.
* Monitor course enrollments.

---

## Tech Stack

### Frontend

* React.js
* Redux (Optional)
* Bootstrap / CSS

### Backend

* Flask
* Flask RESTful APIs
* Flask-JWT-Extended
* SQLAlchemy

### Database

* SQLite (Development)
* PostgreSQL or MySQL (Production)

---

## Database Design

### User

| Field      | Type                  |
| ---------- | --------------------- |
| id         | Integer               |
| email      | String                |
| first_name | String                |
| last_name  | String                |
| password   | String                |
| role       | Enum (Student, Admin) |

Relationships:

* One User can have many Enrollments.
* One User can have many Comments.

### Course

| Field       | Type    |
| ----------- | ------- |
| id          | Integer |
| name        | String  |
| description | Text    |
| price       | Decimal |
| total_hours | Integer |
| rating      | Float   |

Relationships:

* One Course can have many Enrollments.
* One Course can have many Comments.

### Enrollment

| Field      | Type        |
| ---------- | ----------- |
| id         | Integer     |
| student_id | Foreign Key |
| course_id  | Foreign Key |

Relationships:

* Belongs to one User.
* Belongs to one Course.

### Comment

| Field      | Type        |
| ---------- | ----------- |
| id         | Integer     |
| student_id | Foreign Key |
| course_id  | Foreign Key |
| content    | Text        |

Relationships:

* Belongs to one User.
* Belongs to one Course.

---

## Workflow

### Authentication

1. User registers a new account.
2. User logs in.
3. The system generates a JWT token.
4. The user's role is identified.
5. Access permissions are granted according to the role.

### Student Workflow

1. Browse available courses.
2. Apply filters.
3. View course details.
4. Enroll in a course.
5. Track learning progress.
6. Create course collections.
7. Leave ratings and reviews.

### Admin Workflow

1. Log in as an administrator.
2. Create new courses.
3. Update existing courses.
4. Delete courses.
5. View enrolled students.
6. Monitor course activity.

---

## Project Structure

```text
learning-platform/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── schemas/
│   │   └── config/
│   │
│   ├── migrations/
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── redux/
│   │   └── assets/
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Authentication and Authorization

The platform uses JWT-based authentication.

### Student Permissions

* View courses
* Enroll in courses
* Track progress
* Add ratings and reviews

### Admin Permissions

* Create courses
* Update courses
* Delete courses
* View enrollments

---

## Installation

### Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Linux/Mac

venv\Scripts\activate
# Windows

pip install -r requirements.txt

flask db upgrade

flask run
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Future Enhancements

* Course categories
* Advanced search and filtering
* Video lessons
* Certificates of completion
* Payment integration
* Wishlist functionality
* Instructor accounts
* Real-time notifications
* Analytics dashboard

---

## Author

Developed as a Full-Stack Learning Management System using React and Flask.
