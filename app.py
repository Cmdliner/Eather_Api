import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from api import auth

load_dotenv()

CORS_ORIGIN = os.getenv('CORS_ORIGIN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
REFRESH_TOKEN_SECRET = os.getenv('REFRESH_TOKEN_SECRET')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGIN, ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['Authorization', ],
)

app.include_router(auth.router, prefix='/auth', tags=['auth'])