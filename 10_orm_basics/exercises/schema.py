from pydantic import BaseModel
from datetime import datetime


class UserGet(BaseModel):
    id: int
    gender: int
    age: int
    country: str
    city: str
    exp_group: int
    os: str
    source: str

    class Config:
        orm_mode = True


class PostGet(BaseModel):
    id: int
    topic: str
    text: str

    class Config:
        orm_mode = True


class FeedGet(BaseModel):
    action: str
    post_id: int
    time: datetime
    user_id: int
    user: UserGet
    post: PostGet

    class Config:
        orm_mode = True
