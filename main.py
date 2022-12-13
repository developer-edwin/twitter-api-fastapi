# Python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional


# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FasAPI
from fastapi import FastAPI

app = FastAPI()

# Models


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    eamil: EmailStr = Field(...)


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class UserLogin
    password: str Field (
        ...,
        min_length=8,
        max_length=64
    )


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}