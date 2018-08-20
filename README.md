# Catalog App

A catalog of Sports Equipments.


## Description:

An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have ability to post, edit and delete their own items.


## Requirements:

- [Python 2.7](https://www.python.org/)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Flask](http://flask.pocoo.org)
- [SQLAlchemy](http://www.sqlalchemy.org)

As the app uses Google for authentication as the next step you have to obtain a client_secrets.json from Google:

1. Go to the [Google Developer Console](https://console.developers.google.com/project).
2. Create a new project.
3. Go to **APIs & auth - Consent screen** and select a valid Email address.
4. Go to **APIs & auth - Credentials** and create a new Client ID.
5. Enter **http://localhost:8000** in the **Authorized redirect URIs** field.
6. Download the client_secrets.json and store it under /vagrat/catalog directory.


## How to run:

1. Create database tables:

	python models.py

2. Populate the database tables:

	python populatedb.py

3. Run the application:

	python application.py

4. Access application by visiting:
	
	http://localhost:8000/ OR http://localhost:8000/catalog
