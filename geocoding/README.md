# Geocoding Service

We create a simple Network Service that can resolve the provided latitude and longitude into an address using third party geocoding services.

The third party services used are HERE and Bing:

- HERE: `https://developer.here.com/documentation/geocoder/topics/quick-start.html`
- Bing: `https://msdn.microsoft.com/en-us/library/ff701713.aspx`

Our Network Service will use HERE as the primary service and it will fall back to Bing in case no result is found or Network Error

## Required Softwares:
- Python 3.6
- pip3
- virtualenv
- Django = 2.1.3 
- djangorestframework = 3.8.2
- django-environ = 0.4.5
- urllib3 = 1.24.1
- requests = 2.20.0

## Setup steps:

### Using MacOS:

Install python3.6 using package installer:

```https://www.python.org/downloads/mac-osx/```

Install pip:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py

```

Install virtualenv:

```
pip3 install virtualenv
```

### Using Ubuntu 18.04:

Install python 3.6:

```
sudo apt-get install python3
```

Install pip3:

```
sudo apt-get install python3-pip
```

Install virtualenv:

```
sudo apt-get install virtualenv
```

### Starting Server:

- Enable virtual environment:

```virtualenv geocoding -p python3```

- Navigate into `geocoding` directory and activate the virtual environment

```source bin/activate```

- Install `Django` and dependencies to run the service:

```pip install -Ur requirements/development.txt```

- Run the http server:

```python manage.py runserver```

You should see something like this:

```
Performing system checks...
   
System check identified no issues (0 silenced).
November 03, 2018 - 22:40:44
Django version 2.1.3, using settings 'config.settings.development'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

- To stop server, simply use `CTRL+C` and run `deactivate` to get out of the current virtual environment

### How to access Geocoding API:

- From web browser and use the follow URL: 

```http://http://localhost:8000/api/v1/location?latitude={your_latitude}&longitude={your_longitude}```

- Using curl command:

```curl "http://http://localhost:8000/api/v1/location?latitude={your_latitude}&longitude={your_longitude}""```

- To read information about the app, simply hit the base URL:

```curl http://localhost:8000```

### Testing:

There are two test files one for the ```geocoder_service.py``` and one for ```geo_location_view.py```.
To run the full suite, make sure you repeat the step above to activate the virtual environment then run:

```python manage.py test app```

You should see something like this:

```
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 1.804s
```

### Understanding The Project Structures:

Python follow the MVT (Model - View - Template) architecture which is very similar to MVC (Model - View - Controller)

- ```geocoding``` directory is the root of our application:
- ```config``` directory is a "project" in Django framework and ``app`` directory is the application 
- ```config``` has all environment configuration settings we have for the service
- ```config/settings``` directory contains settings for development, production and test environment. For now, we only populate development.py
- ```app``` is the core of our service:
  - ```app/services``` contains all services that encapsulate business logic and are invoked in Views  
  - ```app/models``` contains all application models (ORM objects). For now, we don't have any models
  - ```app/migrations``` contains all migrations for Database which we don't use for now
  - ```app/views``` contains all views that define our REST API. 
  - ```app/templates``` contains rendering templates for all endpoints. For now, we don't have any template.
  - ```app/tests``` contains all test cases for services, models, and views
  - ```urls.py``` defines all routes that are available in our application.
- ```requirements``` contains libraries that each environment needs to run the application
- ```manage.py``` is the interface file that help us interact with Django framework.

