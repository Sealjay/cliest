from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
    DateTime,
    Boolean,
    Integer,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from dotenv import dotenv_values
import pyodbc
from sqlalchemy.sql.sqltypes import DateTime
import misc

config = misc.get_relative_config()
server = config["DB_SERVER"]
database = config["DB_NAME"]
username = config["DB_ADMIN_LOGIN"]
password = config["DB_ADMIN_PW"]
pyodbc.pooling = False

# declarative base class
Base = declarative_base()


class Tweets(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    tweet = Column(String)
    is_posted = Column(Boolean)
    is_scheduled = Column(Boolean)
    schedule_date = Column(DateTime)


class Tweet_Hashtags(Base):
    __tablename__ = "tweet_hashtags"
    id = Column(Integer, primary_key=True)
    hashtag = Column(String)


def connect_to_database():
    engine = create_engine(
        f"mssql+pyodbc://{username}:{password}@{server}/"
        + f"{database}?driver=ODBC+Driver+17+for+SQL+Server",
        echo=True,
    )
    return engine