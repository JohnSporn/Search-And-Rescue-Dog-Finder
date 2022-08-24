# Search-And-Rescue-Dog-Finder

Search-And-Rescue-Dog-Finder - Python
 
A mock app to help identify dogs for search-and-rescue training using a NoSQL Database.

About the Project/Project Title
Our software team has been assigned to work on a system for an innovative international rescue-animal training company, Grazioso Salvare. Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. This is a system that will work with existing data from the animal shelters to identify and categorize available dogs to train for search and rescue. The application will include a database and a client-facing web application dashboard.

Motivation
The system will be used to identify dogs through five animal shelters that are good candidates to be trained in search-and-rescue. Once trained the dogs will be used to help find and rescue humans and other animals in life threatening situations such as locating someone after a disaster has occurred. The system will help identify specific dog breeds for each type of rescue.	

Getting Started
Users will need to download the project files and open them in a python IDE. 

They will also need to open their command prompt and import the animal data set CSV file using the mongoimport tool:
 

Then they will need to authenticate a user for the database by first creating an administrator account and then creating a user account for the AAC database:
 
 

Now the application is ready to go.

Installation
The system requires a few tools to use the application. First, install Mongodb and the latest version of Python. Then download the following extensions through the command prompt:
•	pip install pymongo
•	pip install jupyter_plotly_dash
•	pip install dash
•	pip install pandas

Download the project files to your computer. This includes the AnimalShelter.py file and the ApplicationDashboard.ipynb file.

Usage
This project will be used as a framework for users to store and process animal data for search and rescue training. The use of pymongo and jupyter_plotly_dash allowed us to create an easy-to-use user interface to make these processes easier for the user.

Code Example
CRUD: AnimalShelter class

 
 


Front-end code snippets for dashboard:

Importing AnimalShelter.py CRUD class into the ApplicationDashboard.ipynb file
 

Code for drop down menu above data table
 

Queries for finding rescue specific breeds
 
 


Dashboard Screenshots

Default view of Dashboard
 
 
 

Query for water rescue dogs
  

Query for mountain and wilderness rescue dogs
 
 

Query for disaster or individual tracking rescue dogs
 

Resetting data table to default
 

Geolocation change upon row selection
 

 

Roadmap/Features 
Future features will provide multiple marker locations to pop up on map. Adding the ability to select multiple rows and displaying each individual location of selected rows on map.
