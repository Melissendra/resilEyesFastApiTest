from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine


import logging

_logger = logging.getLogger(__name__)

_logger.info('Creating Database')
models.Base.metadata.create_all(engine)

app = FastAPI()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/users/', response_model=List[schemas.User], status_code=status.HTTP_200_OK)
def read_users(db: Session = Depends(get_db)):
    # Get the list of users
    return crud.get_all_users(db)

@app.post('/users/', response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    # Create a new user
    return crud.create_user(db=db, user=user)

@app.get('/users/{user_id}', response_model=schemas.User, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # Get an user's information
    db_user = crud.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found.')
    return db_user

@app.put('/users/{user_id}', response_model=schemas.User, status_code=status.HTTP_200_OK)
def user_update(user_id: int, user: schemas.User, db: Session = Depends(get_db)):
    # Update some user's information
    return crud.update_user(db=db, user_id=user_id, user=user)

@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Delete an user by id
    crud.delete_user(db=db, user_id=user_id)
    return {
        'status': 200,
        'transaction': 'Success'
    }