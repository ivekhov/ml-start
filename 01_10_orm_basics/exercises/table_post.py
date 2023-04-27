from sqlalchemy import Column, Integer, Boolean, String
from database import Base, engine, SessionLocal


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, name='id')
    topic = Column(String, name='topic')
    text = Column(String, name='text')


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = SessionLocal()
    posts_top = (
        session.query(Post)
        .filter(Post.topic == 'business')
        .order_by(Post.id.desc())
        .limit(10)
        .all()
    )
    posts_id = [post.id for post in posts_top]
    print(posts_id)
