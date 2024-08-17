# [Eather](https://eather-iota.vercel.app)

Backend API for the Eather platform

## Technologies used

- Python
- FastAPI
- Passlib
- MySql (Maria DB)
- Docker

## BUGS

## TODO

- Appointment works (created in rogue dev mode) refactor and handle errors properly
- Results are a one-to-one relationship to Appointments
- Try doing Price Locale Conversion
- Implement error handling properly

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

### Create a .env file at the project root using template by running:

```sh
chmod u+x scripts/create_env.sh  && ./scripts/create_env.sh
```

### Database Operations

- Ensure that database in the env file is already created. If not create it now.
- Run database migrations

#### Database Migrations

```py
#!/bin/python3
from models.base import Base
from config.db import engine


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    print("Creating tables...")
    init_db()
    print("DONE :)")

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
│   ├── appointment.py
│   ├── base.py
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
