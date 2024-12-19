# my_flask_app

## Creating a 3-tier web application in Python involves three distinct layers:

    Presentation Layer (Frontend) - A web interface that allows users to interact with the application.
    Business Logic Layer (Backend) - Where the core logic of the application is processed.
    Data Layer - Where the data is stored, typically in a database.


We'll use Flask for the frontend and backend, and SQLite for the data layer as a simple, lightweight option. You can later upgrade the data layer to PostgreSQL or MySQL as needed.

Here’s the structure of the application:

    Frontend (HTML, CSS, and JavaScript via Flask routes).
    Backend (Python using Flask for handling HTTP requests).
    Database (SQLite, accessed using SQLAlchemy).


##1. Project Structure

*my_flask_app/
│
├── app/
│   ├── __init__.py          # Initialize the Flask app
│   ├── routes.py            # Define the routes for the web app
│   ├── models.py            # Define the database models
│   ├── templates/
│   │   ├── index.html       # Home page
│   └── static/
│       ├── style.css        # Styles
│       └── script.js        # Optional JavaScript
├── config.py                # Configuration file (for database, etc.)
├── requirements.txt         # Python dependencies
└── run.py                   # Run the application


##2. Steps to Run

    Install Dependencies: Make sure you have Python 3 installed. Then, create a virtual environment and install the dependencies.

python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt

Create the Database: Open a Python shell and create the database tables.

python
>>> from app import db
>>> db.create_all()

Run the Application: Run the application with the following command:

python run.py

Access the Web Application: Open a browser and visit http://127.0.0.1:5000/ to view the app.
