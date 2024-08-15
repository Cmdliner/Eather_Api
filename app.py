from api import auth, test, appointment
from config.settings import settings
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from middlewares.auth import require_auth

load_dotenv()

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization"],
)


@app.get("/healthz")
def check_server_status():
    return {"mssg": "Server is up and running"}


@app.get("/protected")
def test_auth_middleware(_: None = Depends(require_auth)):
    return {"success": "Authenticated"}


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(test.router, prefix="/test", tags=["test"])
app.include_router(appointment.router, prefix="/appointment", tags=["appointment"])
