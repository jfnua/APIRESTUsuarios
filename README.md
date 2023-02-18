## Table of contents

- [General info](#general-info)
- [Setup](#setup)

## General info

Django default system for users, using django rest framework.

## Setup

To run this project:

1. install it locally requirements.txt, run

```
$ pip install -r requirements.txt
```

2. In file mascore/settings/dev.py set params for the database

3. Make migrations and migrate database.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

4. Create superuser

```
$ python manage.py createsuperuser
```

5. run server

```
$ python manage.py runserver
```

The server default run in port 8000
Admin site: http://127.0.0.1:8000/admin
API documentation: http://127.0.0.1:8000/redoc/ or http://127.0.0.1:8000/swagger/
