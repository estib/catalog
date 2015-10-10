# catalog
Project 3 for Udacity Fullstack Nanodegree 


NB: the home page of this app is "http://localhost:8000/catalog"


Project name:

"Udacity_Project_3"


Use:

This app locally hosts a catalog of categorized items on port 8000.

All users can use the app to see a list of categories in the catalog, and a
list of items within each category. Upon selecting each item, the user can find
the description given by the whichever user created the item. All users can
access the full catalog's JSON by going to the /catalog/json url.

Only users who have logged in with a google plus account can add or delete
categories to the catalog. Logged in users can only delete those categories
that they have created. Similarly, only logged in users can add, delete, or
edit items in the categories, and they can only delete or edit those items
that they created.

(One exception: if a user-A deletes a category that that user-A created, then
they will also delete any items in that category that any non-user-A created.)


How to run:

The user ought to have access to a vagrant account and should be connected to
the appropriate ssh where they can access the files for this project. The user
will have to run PSQL and create a database called "catalog_db" if such a
database does not yet exist.

The following files should be found in the directory:

1. db_setup.py (will populate the "catalog_db" database)
2. application.py (contains all CRUD and Flask framework functions)
3. page_design.py (contains all functions for creating html content)
4. /static/catalog.css (the style-guide that the project's html uses)
5. client_secrets.json (contains data for google plus sign-in)

If the database does not yet exist, the user must first create a database
called "catalog_db" and then run "db_setup.py" to set up the database. Then
the user can run "application.py" and go to "http://localhost:8000/catalog"
to use the application.


Author:

all files in this project were written by Stephen Lechner.
