import pyodbc
import requests
import json
from schema import (
    connect_to_database,
    Base,
    Tweet_Hashtags,
    Tweets,
)
from sqlalchemy.orm import sessionmaker
from PyInquirer import prompt
import misc

config = misc.get_relative_config()


def create_session():
    engine = connect_to_database()
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session


def interactive_prompt_loop():
    session = create_session()

    if not "id" in prompt_output:
        click.secho("ID not found, cancelling.", fg="bright_red")


def interactive_prompt(session):
    """questions = [
        {
            "type": "list",
            "message": "What do you want to do?",
            "name": "function",
            "choices": [
                {
                    "name": "Add Tweet from Scratch",
                    "value": o365.print_tabulated_calendar,
                },
                {
                    "name": "Open Calendar (open-cal)",
                    "value": o365.prompt_to_open_calendar_event,
                },
                {"name": "View Tasks", "value": o365.get_tasks},
                {"name": "Open Music", "value": music.prompt_to_select_station},
            ],
        }
    ]"""
    prompt_output = prompt(questions)
    if "function" in prompt_output:
        prompt_output["function"]()


def create_plain_tweet(session):
    pass


def prompt_hashtags(tweet_text):
    pass


def prompt_by_term():
    pass


def prompt_by_trending():
    pass


def prompt_by_category():
    pass


def add_tweet_to_schedule(text, session):
    new_tweet = Tweets(text=text)
    session.add(new_tweet)
    session.commit()
    return new_tweet


def find_news_articles(topic):
    return None


def add_hashtags(hashtag_text, session):  # , session):
    new_hashtag = Tweet_Hashtags(hashtag=hashtag_text)
    session.add(new_hashtag)
    session.commit()
    return new_hashtag


def delete_hashtags(hashtag_id):
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