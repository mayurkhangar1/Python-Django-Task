Project Name :- Library Management System using Django
Description :- This project implements a web-based library management system using Django, 
allowing administrators to manage books, authors, and borrowing records. 
It includes features for adding, editing, and exporting data to Excel.

Set up:-
1) Clone the Repository:- To clone the project from the Repository
   git clone https://github.com/mayurkhangar1/Python-Django-Task.git
2) install dependencies:- To install project dependencies using pip
   pip install -r requirements.txt
3) apply migration:- to set up the database schema
   python manage.py migrate
4) run the server:- to start the development server
   python manage.py runserver

Usage :- Access the Django admin interface at `http://localhost:8000/admin/` to manage Authors, Books, and Borrow Records.
Use the provided forms to add new entries or edit existing ones.
-Navigate to the following URLs to view paginated lists:
  - Authors: `http://localhost:8000/authors/list/`
  - Books: `http://localhost:8000/books/list/`
  - Borrow Records: `http://localhost:8000/borrows/list/`
- To export all data to Excel sheets:
  `http://localhost:8000/export/`
