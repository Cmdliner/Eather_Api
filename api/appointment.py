from config.db import get_db
from datetime import datetime, UTC
from fastapi import APIRouter, Depends, status, HTTPException, Request
from middlewares.auth import require_auth
from models.appointment import Appointment
from models.user import User
from models.test import Test
from schemas.appointment import Appointment as AppointmentSchema
from sqlalchemy.orm import Session
from utils.auth_helpers import get_current_user


router = APIRouter(dependencies=[Depends(require_auth)])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def new_appointment(
    appointment: AppointmentSchema, req: Request, db: Session = Depends(get_db)
):
    try:
        authToken = req.headers.get("Authorization").split(" ")[-1]
        user_email = get_current_user(authToken)
        print(user_email)
        user = db.query(User).filter(User.email == user_email).first()

        if not user:
            raise HTTPException(
                detail="User not found", status_code=status.HTTP_404_NOT_FOUND
            )
        new_appointment = Appointment(
            user_id=user.id,
            duration=datetime.now(UTC),
            patient_complaints=appointment.patient_complaints,
            price_total=appointment.price_total,
        )
        # Get tests from the list and added them to the new appointment
        # new_appointment.tests.append()
        #! TODO => HANDLE ERORORS HERE IF NO TESTS
        tests = db.query(Test).filter(Test.id.in_(appointment.tests)).all()
        if not tests:
            raise HTTPException(detail="Invalid appointments details", status_code=400)
        new_appointment.tests.extend(tests)
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        return {"success": "Appointment created successfully"}
    except Exception as err:
        print(err)
        raise HTTPException(detail="Internal server error", status_code=500)


@router.get("/{appointment_id}/details")
async def get_appointment_details(appointment_id: str, db: Session = Depends(get_db)):
    try:
        appointment = (
            db.query(Appointment).filter(Appointment.id == appointment_id).first()
        )
        print(f"Apointment -> {appointment}")
        if appointment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found"
            )
        return appointment
    except Exception as err:
        print(err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting appointment details",
        )


@router.get("/my-appointments")
async def get_all_user_appointments(req: Request, db: Session = Depends(get_db)):
    try:
        authToken = req.headers.get("Authorization").split(" ")[-1]
        if authToken is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
            )
        user_email = get_current_user(authToken)
        user = db.query(User).filter(User.email == user_email).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized"
            )

        user_appointments = (
            db.query(Appointment).filter(Appointment.user_id == user.id).all()
        )
        return user_appointments
    except Exception as err:
        print(err)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error getting user appointments",
        )
