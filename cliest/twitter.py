import pyodbc
import requests
import json
from schema import (
    connect_to_database,
    Base,
    Tweet_Hashtags,
    Tweets,
    News_Article,
    News_Topics,
    tweet_hashtag_association_table,
)
import misc

config = misc.get_relative_config()


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


def search_bing_by_term(search_term):
    params = {"q": search_term, "textDecorations": False}
    search_results = search_bing("/search", params)
    return search_results


def search_bing_by_category(category="ScienceAndTechnology", market="en-GB"):
    search_results = search_bing(f"?mkt={market}&category={category}")
    return search_results


def search_bing_by_trending(market="en-GB"):
    search_results = search_bing(f"/trendingtopics?mkt={market}")
    return search_results


def search_bing(query_string="", params={}):
    subscription_key = config["BING_SEARCH_KEY"]
    search_url = config["BING_SEARCH_ENDPOINT"] + f"v7.0/news{query_string}"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    return search_results