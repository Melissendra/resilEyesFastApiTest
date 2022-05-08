import email
from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    """ Declaration of our user's table"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    phone = Column(String)
    birthday = Column(String)

    def __repr__(self) -> str:
        # This table will be represent by a string
        return f"<User firstname={self.firstname} lastname={self.lastname}"