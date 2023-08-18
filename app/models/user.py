from typing import Optional

from beanie import Document, init_beanie
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, validator

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Document):
    id: Optional[str]
    email: EmailStr
    username: str
    hashed_password: str

    @validator("email")
    def validate_email(cls, email):
        # TODO: Check if the email is already in use in the database
        # Assuming a hypothetical function check_email_exists
        # if check_email_exists(email):
        #     raise ValueError("Email is already in use.")
        return email

    @classmethod
    def create(cls, email: EmailStr, username: str, password: str):
        hashed_password = pwd_context.hash(password)
        return cls(email=email, username=username, hashed_password=hashed_password)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.hashed_password)

# This is a placeholder; the actual logic for checking email uniqueness will depend on the database setup and Beanie usage.
def check_email_exists(email: EmailStr) -> bool:
    # Placeholder logic; replace with actual database check
    return False
