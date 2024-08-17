from config.db import get_db
from datetime import datetime, UTC
from fastapi import APIRouter, Depends, status, HTTPException, Request
from models.appointment import Appointment
from models.user import User
from models.test import Test
from schemas.appointment import Appointment as AppointmentSchema
from sqlalchemy.orm import Session
from utils.auth_helpers import get_current_user


router = APIRouter()


@router.post("/create", status_code=status.HTTP_201_CREATED)
def new_appointment(
    appointment: AppointmentSchema, req: Request, db: Session = Depends(get_db)
):
    # appointment = appointment.model_dump()
    try:
        user = db.query(User).filter(User.id == appointment.user_id).first()

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
        # Get tests from the lise and added them to the new appointment
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
