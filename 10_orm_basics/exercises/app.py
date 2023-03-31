from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import func
from typing import List
from database import Base, engine, SessionLocal
from schema import UserGet, PostGet, FeedGet
from table_user import User
from table_post import Post
from table_feed import Feed


app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get('/post/recommendations/')
def get_post_reco(limit: int = 10, db: SessionLocal = Depends(get_db)):
    # posts = (
    #     db.query(Feed.post_id, func.count("*"))
    #     .filter(Feed.action == 'like')
    #     .group_by(Feed.post_id)
    #     .order_by(func.count("*").desc())
    #     .limit(limit)
    #     .all()
    # )

    posts = (
        db.query(Post)
        .select_from(Feed)
        .filter(Feed.action == 'like')
        .join(Post)
        .group_by(Post.id)
        .order_by(func.count(Feed.post_id).desc())
        .limit(limit)
        .all()
    )
    if not posts:
        raise HTTPException(404, 'posts not found')
    else:
        return posts


@app.get('/user/{id}/feed', response_model=List[FeedGet])
def get_users_feed(id: int, limit: int = 10, db: SessionLocal = Depends(get_db)):
    user_feed = (db
                 .query(Feed)
                 .filter(Feed.user_id == id)
                 .order_by(Feed.time.desc())
                 .limit(limit)
                 .all()
                 )
    if not user_feed:
        raise HTTPException(200, [])
    else:
        return user_feed


@app.get('/post/{id}/feed', response_model=List[FeedGet])
def get_posts_feed(id: int, limit: int = 10, db: SessionLocal = Depends(get_db)):
    user_feed = (db
                 .query(Feed)
                 .filter(Feed.post_id == id)
                 .order_by(Feed.time.desc())
                 .limit(limit)
                 .all()
                 )
    if not user_feed:
        raise HTTPException(200, [])
    else:
        return user_feed


@app.get('/user/{id}', response_model=UserGet)
def get_user(id: int, db: SessionLocal = Depends(get_db)):
    Base.metadata.create_all(engine)
    user = db.query(User).filter(User.id == id).one_or_none()
    if not user:
        raise HTTPException(404, "user not found")
    else:
        return user


@app.get('/post/{id}', response_model=PostGet)
def get_post(id: int, db: SessionLocal = Depends(get_db)):
    Base.metadata.create_all(engine)
    post = db.query(Post).filter(Post.id == id).one_or_none()
    if not post:
        raise HTTPException(404, "post not found")
    else:
        return post
