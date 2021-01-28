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

config = dotenv_values(".env")
server = config["DB_SERVER"]
database = config["DB_NAME"]
username = config["DB_ADMIN_LOGIN"]
password = config["DB_ADMIN_PW"]
pyodbc.pooling = False

# declarative base class
Base = declarative_base()

tweet_hashtag_association_table = Table(
    "tweet_hashtag_association",
    Base.metadata,
    Column("tweet_id", Integer, ForeignKey("tweets.id")),
    Column("hashtag_id", Integer, ForeignKey("tweet_hashtags.id")),
)


class Tweets(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True)
    tweet = Column(String)
    is_posted = Column(Boolean)
    is_scheduled = Column(Boolean)
    schedule_date = Column(DateTime)
    tweet_hashtags = relationship(
        "Tweet_Hashtags",
        secondary=tweet_hashtag_association_table,
        back_populates="tweet_hashtags",
    )


class Tweet_Hashtags(Base):
    __tablename__ = "tweet_hashtags"
    id = Column(Integer, primary_key=True)
    hashtag = Column(String)
    tweets = relationship(
        "Tweets", secondary=tweet_hashtag_association_table, back_populates="tweets"
    )


class News_Article(Base):
    __tablename__ = "news_article"
    id = Column(Integer, primary_key=True)
    article_name = Column(String)
    article_url = Column(String)
    related_topic_id = Column(Integer, ForeignKey("news_topic.id"))
    related_topic = relationship("News_Topic")


class News_Topics(Base):
    __tablename__ = "news_topic"
    id = Column(Integer, primary_key=True)
    topic_name = Column(String)


def connect_to_database():
    engine = create_engine(
        f"mssql+pyodbc://{username}:{password}@{server}/"
        + f"{database}?driver=ODBC+Driver+17+for+SQL+Server",
        echo=True,
    )
    return engine