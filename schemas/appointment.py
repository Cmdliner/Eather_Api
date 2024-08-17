from datetime import datetime
from pydantic import BaseModel
from typing import List


class Appointment(BaseModel):
    user_id: str
    patient_complaints: str
    price_total: int
    tests: List[str] | None = None
