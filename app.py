import os
from api import auth, test
from config.settings import settings
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from middlewares.auth import require_auth

load_dotenv()

CORS_ORIGIN = os.getenv("CORS_ORIGIN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz")
def check_server_status():
    return {"mssg": "Server is up and running"}


@app.get('/protected')
def test_auth_middleware(_: None = Depends(require_auth)):
    return {"success": "Authenticated"}

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(test.router, prefix="/test", tags=["test"])
