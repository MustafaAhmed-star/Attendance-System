# Attendance System                      

## Overview

The Attendance System is a Django-based web application designed to manage attendance records for students and doctors. It provides features for recording attendance, viewing timetables, and managing subjects and levels.

## Features

- **User Authentication:** Login and access control for students and doctors.
- **Role-based Dashboard:** Separate dashboards for students and doctors.
- Attendance Management:
  - Record attendance for each subject.
  - View attendance records for students.
- Timetable Management:
  - Upload timetables for doctors and students.
  - Display timetables based on user role.
- Subject Management:
  - Manage subjects associated with students and doctors.
  - View subjects by level.
- **Level Management:** Associate students and doctors with different levels.
- **Department Management:** Manage and assign departments.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (or any preferred database)
- Git

### Installation

1. **Clone the repository:**

   ```
   bashCopy codegit clone https://github.com/MustafaAhmed-star/Attendance-System.git
   cd Attendance-System
   ```

2. **Create and activate a virtual environment:**

   ```
   bashCopy codepython -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```
   bash
   Copy code
   pip install -r requirements.txt
   ```

4. **Configure the database:** Update the `DATABASES` settings in `settings.py` to match your database configuration.

5. **Apply migrations:**

   ```
   bash
   Copy code
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```
   bash
   Copy code
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```
   bash
   Copy code
   python manage.py runserver
   ```

8. **Access the application:** Open your browser and go to `http://127.0.0.1:8000`.

## Project Structure

- **core:** Contains the main settings and configuration for the Django project.
- **media:** Directory for user-uploaded media files.
- **project:** Contains the main application code.
- **static:** Directory for static files (CSS, JavaScript, images).
- **templates:** HTML templates for the project.
- **users:** User management and authentication.

## Key Models

- **Person:** Abstract base model for `Doctor` and `Student`.
- **Doctor:** Model for doctors, extends `Person`.
- **Student:** Model for students, extends `Person`.
- **Subject:** Model for subjects.
- **Department:** Model for departments.
- **Level:** Model for levels.
- **Attendance:** Model for attendance records.
- **TimeTable:** Model for timetables.

## Views

- **home:** Renders the homepage.
- **lec_attendance:** Displays attendance for a specific subject.
- **submit_attendance:** Submits attendance for a subject.
- **subjects_by_level:** Lists subjects by level for a doctor.
- **view_attendance:** Displays attendance records for a student.
- **user_timetable:** Displays the timetable for the logged-in user.

## Templates

- **base.html:** Base template for the project.
- **home.html:** Template for the homepage.
- **attendance/lec_attendance.html:** Template for displaying attendance.
- **students/student_attendance.html:** Template for student attendance view.
- **time_table.html:** Template for displaying timetables.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
