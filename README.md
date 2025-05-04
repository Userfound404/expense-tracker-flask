# Personal Expense Tracker

A Flask-based web application for tracking personal expenses, designed and built as part of an evaluation test. The app allows users to register, log in, manage expense categories, add/edit/delete expenses, view interactive visualizations, and export data.

---

## Features I've added

* **User Auth**: Register, log in, and log out using `Flask-Login`.
* **Expense CRUD**: Create, read, update, and delete expenses, each with a date, description, category, and amount.
* **Category Management**: Create and list custom categories to organize expenses.
* **Interactive Chart**: Visualize spending by category with a `Chart.js` pie chart.
* **Summary Cards**: See high-level metrics—total spent and money left based on a default budget (set at 80000).
* **CSV Export**: Download all expenses as a CSV file for external analysis or backup.
* **Responsive UI**: Built with Bootstrap 5 for mobile and desktop friendly layouts.

## Tech Stack

* **Backend**: Python, Flask, Flask-Login, Flask-WTF, Flask-Migrate
* **ORM & DB**: SQLAlchemy, SQLite (default; switchable to PostgreSQL)
* **Frontend**: Jinja2 templates, Bootstrap 5, Chart.js
* **Environment**: Python virtual environment (`venv`)

SQLite was my first choice, as this would not go to production and the scale of CRUD is very small.
This should be switchable to PostgreSQL for production

## Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/expense-tracker-flask.git
   cd expense-tracker-flask
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database** (SQLite by default)

   ```bash
   flask db upgrade
   ```

5. **Run the application**

   ```bash
   python run.py
   ```

6. **Access the app**
   Open `http://127.0.0.1:5000/` in your browser, register a new account, and start tracking expenses!

## Project Structure

```
expense_tracker/
├─ app/
│  ├─ auth/            # Blueprint for authentication
│  ├─ expenses/        # Blueprint for expense & category management
│  ├─ models.py        # SQLAlchemy models
│  ├─ forms.py         # WTForms definitions
│  ├─ templates/       # Jinja2 templates
│  └─ __init__.py      # App factory & extension setup
├─ migrations/         # Database migration scripts
├─ sample_data/        # (Optional) JSON files for seeding data
├─ config.py           # App configuration & default budget
├─ run.py              # Application entry point
├─ requirements.txt
└─ README.md
```

## Personal Approach & Experience

I built this project step-by-step to demonstrate full-stack capabilities:

1. **Environment Setup**: Initialized a Python `venv`, installed Flask and extensions.
2. **App Factory**: Used the factory pattern in `app/__init__.py` for easy testing and configuration. (This was the first time I read about this)
3. **Models & Migrations**: Defined `User`, `Category`, and `Expense` models with SQLAlchemy and managed schema changes via Flask-Migrate. I've changed the schema you provided, just to make it a bit more useful.
4. **Authentication**: Implemented secure registration and login flows using `Flask-Login` and `Flask-WTF` for form validation.
5. **CRUD Operations**: Created blueprints for modular routing and handled create/read/update/delete for categories and expenses.
6. **UI & UX**: Chose **Bootstrap 5** to ensure responsiveness without hand-coding media queries.
7. **Visualization**: Integrated **Chart.js** for interactive pie charts, providing insights into spending patterns.
8. **Extras**: Added summary cards for quick metrics, CSV export for data portability, and edit/delete functionality for full CRUD.

Throughout, I focused on code readability, modular organization, and user-friendly design—key factors in a production-ready evaluation.

## Design Decisions

* **Flask**: Lightweight microframework that combines simplicity with powerful extensions.
* **SQLAlchemy**: ORM for productive database interactions and easy migrations.
* **Bootstrap 5**: Rapidly implement a consistent, responsive UI without custom CSS.
* **Chart.js**: Simple yet flexible charts that integrate nicely with Flask templates.

## Outputs and features

1. **Login**

![login](https://github.com/user-attachments/assets/0dda0f80-c7b3-4e7f-b2c5-6c299734aaf6)

2. **Adding categories**

![adding categories](https://github.com/user-attachments/assets/fe65c57d-07cc-433f-84a3-69279197b307)

3. **Adding Expenses**

![adding expenses](https://github.com/user-attachments/assets/341a1004-47e6-4755-a05c-349f74aa0f69)

4. **Editing and Deleting Expenses**

![Editing and deleting expenses](https://github.com/user-attachments/assets/70ec77b0-8b15-47d0-bb6e-5f726bce704e)


