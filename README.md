# Django-CRUD-API
This is a simple Rest API created with [Django REST framework](http://www.django-rest-framework.org/)

## Requirements
- Python 3.9.13
- Django 4.1.3
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv drf_env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, PATCH, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In this case, we have three resources, `employee` `register` `login`, so we will use the following URLS - `/api/employee/` `/api/register/` and `/api/login/` respectively:

## Routes to Implement
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *GET* | ```/api/employee/``` | _Get all employees_|_All users_|
| *POST* | ```/api/employee/``` | _Create a new employee_|_All users_|
| *PUT* | ```/api/employee/``` | _Update an employee_|_All users_|
| *PATCH* | ```/api/employee/``` | _Update an employee attribute_|_All users_|
| *DELETE* | ```/api/employee/``` | _Delete an employee_|_All users_|
| *POST* | ```/api/register/``` | _Register new user_| _All users_|
| *POST* | ```/api/login/``` | _Login user_|_Superuser_|

## Use
We can test the API using [Postman](https://www.postman.com/)

First, we have to start up Django's development server.
```
python manage.py runserver
```

First we need to create a user, so we can log in
```
POST http://127.0.0.1:8000/api/register/ email="email@email.com" username="username" password="password"
```

After we create an account, we can login with the credentials to get a token

To get a token we need to request
```
POST http://127.0.0.1:8000/api/login/ username="username" password="password"
```

## Restrictions
This CRUD API has some restrictions:
-   The API's can be accessed by anyone as Permissions class is not added
-   Pagination class is not used due to small amount of data in database
-   Resource routing in ModelViewSet is not defined in the project
-   Status Codes are also not implemented in the project

#### Using Permissions class

First we need to add this in settings.py file
```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```
Now we need to import and add to the APIView class where permission is required to access data in views.py file
```
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

Add this to APIView class where TokenAuthentication is required
permission_classes = [IsAuthenticated]
authentication_classes = [TokenAuthentication]

```

#### Using Pagination

First we need to add this in settings.py file
```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}
```
Now we need to import Paginator in views.py file and write the logic in our function
```
from django.core.paginator import Paginator
```

#### Using Routers in ModelViewSet

We need to import viewsets in views.py file and create a ModelViewSet Class
```
from rest_framework import viewsets
```
Now we need to import routers in views.py file and add path in url patterns
```
from rest_framework import routers
```

#### Using Status Codes

We need to import status in views.py file and add status code to our functions
```
from rest_framework import status
```



