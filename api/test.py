from config.db import get_db
from fastapi import APIRouter, Depends, Path, Body, status

# from middlewares.auth import require_auth
from models.test import Test
from schemas.test import Test as TestSchema, TestUpdate
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/all", status_code=200)
def get_all_tests(db: Session = Depends(get_db)):
    all_tests = db.query(Test).all()
    return all_tests


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=TestSchema)
def create_new_lab_test(test: TestSchema, db: Session = Depends(get_db)):
    test_in_db = Test(name=test.name, price=test.price, description=test.description)

    db.add(test_in_db)
    db.commit()
    db.refresh(test_in_db)
    return test


@router.put("/{test_id}/update", response_model=None)
def update_lab_test(
    test_id: str = Path(), updates: TestUpdate = Body, db: Session = Depends(get_db)
):
    test = db.query(Test).filter(Test.id == test_id).first()
    if updates.name:
        test.name = updates.name
    if updates.description:
        test.description = updates.description
    if updates.price:
        test.price = updates.price
    db.commit()
    db.refresh(test)

    #
    updates.name = test.name
    updates.price = test.price
    updates.description = test.description
    return updates


@router.delete("/{test_id}/delete", response_model=None)
def delete_lab_test(test_id: str = Path(), db: Session = Depends(get_db)):
    test_to_delete = db.query(Test).filter(Test.id == test_id).first()

    db.delete(test_to_delete)
    db.flush()
    db.commit()

    return {"success": "Test deleted successfully!"}
