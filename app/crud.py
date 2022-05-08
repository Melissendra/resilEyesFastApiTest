import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

_logger = logging.getLogger(__name__)


def get_user(db: Session, user_id: int):
    # Function to get one user by id
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_users(db: Session):
    # function to get all the users
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.User):
    # Function to create a new user
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if db_user is not None:
        raise HTTPException(status_code=400, detail='An user with this email already exists')

    new_user = models.User(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        phone=user.phone,
        birthday=user.birthday
        )
    # Adding him to db
    db.add(new_user)
    db.commit()
    return new_user

def update_user(db: Session, user_id: int, user: schemas.User):
    # Function to update a user's information
    user_to_update = db.query(models.User).filter(models.User.id == user_id).first()
    user_to_update.firstname = user.firstname
    user_to_update.lastname = user.lastname
    user_to_update.email = user.email
    user_to_update.phone = user.phone
    user_to_update.birthday = user.birthday

    db.commit()
    return user_to_update

def delete_user(db: Session, user_id: int):
    # function to delete a user by id
    db_user_to_delete = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user_to_delete:
        raise HTTPException(status_code=404, detail='User not found.')
    db.delete(db_user_to_delete)
    db.commit()
    return db_user_to_delete
