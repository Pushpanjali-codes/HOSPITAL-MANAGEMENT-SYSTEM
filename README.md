# HOSPITAL-MANAGEMENT-SYSTEM
Hospital Management System in Python using MySQL. Features user registration/login, and CRUD operations for doctors, nurses, workers, and patients via CLI. Data stored in MySQL tables. Simple admin and patient management for small clinics or educational use.

# Hospital Management System

A simple Hospital Management System in Python using MySQL for data storage. This CLI-based application allows user registration/login and management of doctors, nurses, workers, and patients.

## Features

- User registration and login
- Manage doctor, nurse, and worker records (add, view, delete)
- Manage patient records (add, view, discharge)
- Data stored in MySQL tables
- Simple command-line interface

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

## Setup

1. **Install MySQL Server** and ensure it is running.
2. **Install required Python package:**
   ```
   pip install mysql-connector-python
   ```
3. **Run the script:**
   ```
   python main.py
   ```
4. **Enter your MySQL root password** when prompted.

## Usage

- Register a new user or sign in with existing credentials.
- Use the menu to manage hospital staff and patient records.
- All data is stored in a MySQL database (`city_hospitals`).

## Notes

- Make sure your MySQL user has privileges to create databases and tables.
- For educational/demo use only. No password hashing or advanced security.

## License

This project is for educational
