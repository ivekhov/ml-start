from sqlalchemy import Column, Integer, String, func
from database import Base, engine, SessionLocal


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = SessionLocal()
    users = (
        session.query(User.country, User.os, func.count("*"))
        .filter(User.exp_group == 3)
        .group_by(User.country, User.os)
        .having(func.count("*") > 100)
        .order_by(func.count("*").desc())
        .all()
    )
    response = []
    for user in users:
        response.append(user)
    print(response)
