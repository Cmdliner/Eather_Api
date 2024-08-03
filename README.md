# [Eather](https://eather-iota.vercel.app)

Backend API for the Eather platform

## Technologies used

- Python
- FastAPI
- Passlib
- MySql (Maria DB)
- Docker

## BUGS

- Precision error with Price as float (switch to integers and start from smallest unit- Kobo)
- Try doing Price Locale Conversion
## TODO

- Properly implement the auth middleware
- Implement timezone aware datetime (make it consistent accross the entire app)
- Implement test-groups :- E.g. L.F.T, Lipid Profile && Stuff

## How to use

### Create a virtual environment using venv

```sh
python -m venv venv
```

### Activate the virtual environment

For UNIX and Unix-Like systems run:

```sh
source venv/bin/activate
```

For windows run:

```sh
venv\Scripts\activate
```

### Install the dependencies with pip

```sh
pip install -r requirements.txt
```

### Create a .env file at the project root and initalize the following constants

```sh
PROJECT_NAME=Eather
DATABASE_URI=mysql+pymysql://<db_user>:<user_password>@<user_host>/<db_name>
ACCESS_TOKEN_SECRET=<your_access_secret>
REFRESH_TOKEN_SECRET=<your_refresh_secret>
ACCESS_TOKEN_EXPIRE_MINUTES=
```

### Database Operations

- Ensure that database in the env file is already created. If not create it now.
- Run database migrations

#### Database Migrations

```py
#!/bin/python3
from config.db import engine
# from models.user import Base as UserBase
#from models.test import Base as TestBase


def create_tables():
    # UserBase.metadata.create_all(bind=engine)
    #TestBase.metadata.create_all(bind=engine)



if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully")

```

Uncomment all and run the [`create_tables`](#database-migrations) script as shown above in the root of the project directory.

```sh
python create_tables.py
```

### Confirm project structure

At the end of this (with the exception of the .env file and env/ directories) your project should look like this: [`project-structure`](#project-strucure)

### Run the Development Server

```sh
fastapi dev app.py
```

## PROJECT STRUCURE

```sh
.
├── api
│   ├── auth.py
│   ├── __init__.py
│   └── test.py
├── app.py
├── config
│   ├── db.py
│   ├── __init__.py
│   └── settings.py
├── create_tables.py
├── Dockerfile
├── middlewares
│   └── auth.py
├── models
│   ├── __init__.py
│   ├── test.py
│   └── user.py
├── README.md
├── requirements.txt
├── schemas
│   ├── __init__.py
│   ├── test.py
│   └── user.py
└── utils
    ├── auth_helpers.py
    └── __init__.py
```
