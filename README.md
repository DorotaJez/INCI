# INCI analyser

### Table of Contents
* General Information
* Requirements and Setup
* Further Development

### General Information
The INCI Analyser is a simple web application written in Python within the Django framework. As for now, it's functionality is, as the name suggests, to analyse the INCI components of any cosmetic provided by the user and return the information about any potentially dangerous substances. It is inspired by some similar, but more complex web apps (for example the [incidecoder.com](incidecoder.com)). 

### Requirements and Setup
For detailed requirements, please check the requirements.txt file. In general, the app is based on Python 3.10.4 and Django 4.1.4.For the Frontend part of the application, Bootstrap has been applied.
In order to run the app on your local server:
1. Clone the repository and install the required libraries, preferably in a virtual environment
2. Generate a secret key for Django
3. Open the config.py file in the inci_proj folder and set the variable SECRET_KEY to a string of the generated key
4. Navigate to the same directory where the "manage.py" file is located
5. Type "python manage.py runserver" and access the indicated link
There are also some screenshots of the app's layout in the "layout" folder in this repository.

### Further Development
This app was intended to be my first public project on GitHub, so I would highly appreciate any suggestions and corrections. Also, in the future I am planning to come back to this project and implement some of the following ideas:
* Expand the dangerous products database: add more ingredients and elaborate more on them, including a brief description rather than just one word; add reliable sources
* Include "good" or neutral ingredients as well
* Enhance the design and layout