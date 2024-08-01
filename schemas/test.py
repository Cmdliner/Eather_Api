from pydantic import BaseModel, Field
from decimal import Decimal


class Test(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="The test name")
    description: str | None
    price: Decimal = Field(description="The test price")


class TestInDB(Test):
    id: str


class TestUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: str | None = None