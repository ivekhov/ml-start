from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database_creds import SQLALCHEMY_DATABASE_URL
from dotenv import load_dotenv

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# NOTE be careful when sharing

# SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

# SQLALCHEMY_DATABASE_URL = f'postgresql://{$POSTGRES_USER}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
