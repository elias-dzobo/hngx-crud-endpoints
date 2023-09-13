Objective
=========

The objective of this API is to mock the Intern Registration Process for HNGX Interns by recording and manipulating their names and respective tracks.

Setup
=====

1.  Clone the Repository: `git clone [repository link]`
2.  Cd into the cloned directory: `cd directory_name`
3.  Install the required libraries: `pip install -r requirements.txt`
4.  Run: `uvicorn main:app --reload`

Testing
=======

1.  Make sure the server is running.
2.  Run the tests script: `pytest tests.py -v -s`
3.  Or navigate to your local browser and type: `http://127.0.0.1:8000/docs`