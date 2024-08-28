from api import auth, test, appointment
from config.settings import settings
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization"],
    expose_headers=["Authorization"]
)

@app.get("/healthz")
def check_server_status():
    return {"mssg": "Server is up and running"}

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(test.router, prefix="/tests", tags=["test"])
app.include_router(appointment.router, prefix="/appointments", tags=["appointment"])
