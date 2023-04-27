from fastapi import Depends, FastAPI, HTTPException
from datetime import date
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from loguru import logger
from typing import List, Dict

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date
    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    id: int
    text: str
    topic: str


@app.post("/user/validate")
def validate_user(user: User) -> str:
    try:
        return f'Will add user: {user.name} {user.surname} with age {user.age}'
    except:
        raise HTTPException(422)


def get_db():
    conn = psycopg2.connect(
        host="postgres.lab.karpov.courses",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        port=6432,
        database="startml",
        cursor_factory=RealDictCursor
    )
    return conn


@app.get('/user/{user_id}')
def get_user(user_id: int, db=Depends(get_db)):
    # conn = psycopg2.connect(
    #     host="postgres.lab.karpov.courses",
    #     user="robot-startml-ro",
    #     password="pheiph0hahj1Vaif",
    #     port=6432,
    #     database="startml",
    #     cursor_factory=RealDictCursor
    # )
    # conn = get_db()
    # cursor = conn.cursor()

    with db.cursor() as cursor:
        cursor.execute(
            f"""
            select gender, age, city
            from "user"
            where id = {user_id}
            """
        )
        result = cursor.fetchone()
        return result
        if not result:
            raise HTTPException(404, "user not found")
        else:
            return result


@app.get('/post/{id}', response_model=PostResponse)
def get_post(id: int, db=Depends(get_db)) -> PostResponse:
    with db.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT id, text, topic
            FROM post
            WHERE id = {id}
            """
        )
        result = cursor.fetchone()
        if not result:
            raise HTTPException(404, "user not found")
        else:
            return result
        return PostResponse(**result)
