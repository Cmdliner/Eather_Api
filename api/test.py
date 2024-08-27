from config.db import get_db
from fastapi import APIRouter, Depends, Path, Body, HTTPException, status
from middlewares.auth import require_auth
from models.test import Test
from schemas.test import Test as TestSchema, TestUpdate
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session


router = APIRouter(dependencies=[Depends(require_auth)])

@router.get("/all", status_code=200)
async def get_all_tests(db: Session = Depends(get_db)):
    try:
        all_tests = db.query(Test).all()
        return all_tests
    except NoResultFound:
        raise HTTPException(status_code=404, detail="No tests found!")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Error getting tests :(")


@router.get("/{test_id}")
async def get_single_test(test_id: str = Path(), db: Session = Depends(get_db)):
    try:
        test = db.query(Test).filter(Test.id == test_id).first()
        if test:
            return test.name
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Error getting test :(")


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=TestSchema)
async def create_new_lab_test(test: TestSchema, db: Session = Depends(get_db)):
    try:
        test_in_db = Test(
            name=test.name, price=test.price, description=test.description
        )

        db.add(test_in_db)
        db.commit()
        db.refresh(test_in_db)
    except IntegrityError:
        raise HTTPException(
            status_code=422, detail="Test with that name already exists!"
        )
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Error creating test :(")

    return test


@router.put("/{test_id}/update", response_model=None)
async def update_lab_test(
    test_id: str = Path(), updates: TestUpdate = Body, db: Session = Depends(get_db)
):
    try:
        test = db.query(Test).filter(Test.id == test_id).first()
        if updates.name:
            test.name = updates.name
        if updates.description:
            test.description = updates.description
        if updates.price:
            test.price = updates.price
        db.commit()
        db.refresh(test)
    except Exception:
        raise HTTPException(status_code=500, detail="Error updating test :(")

    updates.name = test.name
    updates.price = test.price
    updates.description = test.description
    return updates


@router.delete("/{test_id}/delete", response_model=None)
async def delete_lab_test(test_id: str = Path(), db: Session = Depends(get_db)):
    try:
        test_to_delete = db.query(Test).filter(Test.id == test_id).first()

        db.delete(test_to_delete)
        db.flush()
        db.commit()
    except Exception:
        raise HTTPException(status_code=500, detail="Error deleting test :(")

    return {"success": "Test deleted successfully!"}
