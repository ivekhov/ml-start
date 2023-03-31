from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine, SessionLocal
from table_post import Post
from table_user import User


class Feed(Base):
    __tablename__ = 'feed_action'
    action = Column(String)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    time = Column(DateTime)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user = relationship(User)
    post = relationship(Post)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
