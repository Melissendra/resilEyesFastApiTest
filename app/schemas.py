from pydantic import BaseModel


class User(BaseModel):
    # Our serializer
    id: int
    firstname: str
    lastname: str
    email: str
    phone: str
    birthday: str

    class Config:
        orm_mode=True