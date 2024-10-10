from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Add sslmode=require to the connection URL
SQLALCHEMY_DATABASE_URL = (
    "postgresql://admin:E5OJuKRE14iotwfsvHwJeqsjaKK1eKmO@"
    "dpg-cq0nb2aju9rs73b0500g-a.oregon-postgres.render.com/part2"
    "?sslmode=require"  # Enable SSL
)  # os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
