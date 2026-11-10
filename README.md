🎬 Movie Database Manager


A simple and interactive Movie Database Management System built with Python, Streamlit, and SQLite.


This project provides a user-friendly web interface for managing movie records, allowing users to add, search, view, and update movie information through an interactive dashboard.



📌 Table of Contents




Overview


Features


Technologies


Project Structure


Database Schema


Installation


Run the Application


How to Use


Current Limitations


Future Improvements





📖 Overview


The Movie Database Manager is a Python-based application designed to demonstrate database operations through a Streamlit web interface.


It uses SQLite to store movie information locally and provides several database management operations.


The application separates database functionality from the user interface, making the code easier to understand, maintain, and extend.



✨ Features


📋 View Records




Display all movies stored in the database.


Retrieve a specific movie using its ID.


Search for movies by title.


Search for movies by IMDb rating.




➕ Insert Records




Add new movies to the database.


Store movie titles, release years, countries, and IMDb ratings.




✏️ Update Records




Update movie information using its ID.


Update movie information using its title.




🗑️ Delete Records




Delete movies by title.


When multiple records match a title, select the desired movie using its ID.




💾 Database Management




Store records using SQLite.


Keep database operations separate from the Streamlit interface.


Use reusable functions for CRUD operations.





🛠️ Technologies




Technology
Purpose




Python
Main programming language


Streamlit
Interactive web interface


SQLite
Local database management


sqlite3
Python database connectivity





📁 Project Structure


streamlit_project/
│
├── app_ui.py          # Streamlit user interface
├── app_db.py          # Database operations
├── requirements.txt   # Project dependencies
├── MovieData.db       # Local database (created during initialization)
└── README.md          # Project documentation




🗄️ Database Schema


The application uses an SQLite database named MovieData.db.


The main table is called movies and contains the following columns:




Column
Data Type
Description




id
INTEGER
Unique movie identifier (Primary Key)


title
TEXT
Movie title


year
TEXT
Release year


country
TEXT
Country of origin


imdb_rate
REAL
IMDb rating




Example Record




id
title
year
country
imdb_rate




1
Inception
2010
USA
8.8





⚙️ Installation


Follow these steps to set up the project locally.


1. Clone the Repository


git clone https://github.com/miky619/streamlit_project.git



2. Navigate to the Project Directory


cd streamlit_project



3. Install Dependencies


Install Streamlit:


pip install streamlit





Note: The current requirements.txt file does not contain dependency entries yet.





🚀 Run the Application


Before launching the application, initialize the database table.


Run:


python -c "import app_db; app_db.create_table()"



Then start the Streamlit application:


streamlit run app_ui.py



Streamlit will start a local web server and provide a URL to access the application in your browser.



🖥️ How to Use


After launching the application, use the sidebar menu to access the available operations.


Available Operations




Operation
Description




SELECT ALL RECORDS
Display all movie records


SELECT RECORD BY ID
Find a movie using its ID


SELECT RECORD BY NAME
Search for a movie by title


SELECT RECORD BY RATE
Find movies using IMDb rating


INSERT RECORD
Add a new movie


DELETE RECORD BY NAME
Delete a movie by title


UPDATE RECORD BY ID
Modify a movie using its ID


UPDATE RECORD BY NAME
Modify a movie using its title




Select an operation from the sidebar and follow the instructions displayed in the application.



⚠️ Current Limitations




The database table must be initialized before running the application for the first time.


The requirements.txt file is currently empty.


The Delete by ID option is listed in the sidebar, but its corresponding user-interface functionality has not yet been implemented.





🔮 Future Improvements


Potential improvements for future versions include:




Implementing the Delete by ID interface.


Adding stronger input validation.


Improving error handling and user feedback.


Adding movie sorting and filtering options.


Creating a more advanced and responsive interface.


Adding automated tests.


Improving database initialization and management.





👨‍💻 Author


Miky


GitHub: @miky619




  Built with Python, Streamlit, and SQLite.
  

  A practical project for learning database operations and interactive web applications.



