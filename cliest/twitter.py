import pyodbc
from schema import (
    connect_to_database,
    Base,
    Tweet_Hashtags,
    Tweet,
    News_Article,
    News_Topics,
    tweet_hashtag_association_table,
)


def get_next_tweet():
    return None


def post_tweet(text):
    return None


def find_news_articles(topic):
    return None


def suggest_hashtags_for_topic(topic_id, tweet_text):
    return None


def add_suggested_topic():
    return None


def delete_suggested_topic(topic_id):
    return None


def add_hashtags(topic_id):
    return None


def delete_hashtags(topic_id, hashtag_id):
    return None