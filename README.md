# [Eather](https://eather.onrender.com)

Backend API for the Eather platform 

## Technologies used
- Python
- FastAPI
- Passlib
- Postgresql
- Docker

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
DATABASE_URI=postgresql://<db_user>:<user_password>:5432/<db_name>
ACCESS_TOKEN_SECRET=<your_access_secret>
REFRESH_TOKEN_SECRET=<your_refresh_secret>
ACCESS_TOKEN_EXPIRE_MINUTES=
```

### Run the Development Server
```sh
fastapi run app.py
```
## PROJECT STRUCURE
```sh
.
├── api
│   ├── auth.py
│   └── __init__.py
├── app.py
├── config
│   ├── db.py
│   ├── __init__.py
│   └── settings.py
├── Dockerfile
├── models
│   ├── appointment.py
│   ├── __init__.py
│   ├── payment.py
│   ├── test.py
│   └── user.py
├── README.md
├── requirements.txt
├── schemas
│   ├── __init__.py
│   └── user.py
└── utils
    ├── auth_helpers.py
    └── __init__.py

6 directories, 18 files
```