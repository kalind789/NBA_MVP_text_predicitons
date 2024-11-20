import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('.env')
bearer_token = os.environ.get("Bearer_Token")
client = tweepy.Client(bearer_token=bearer_token)

query = "NBA MVP"
max_results = 10 
excluded_authors = ['TheNBACentel', 'BallsackSports']
start_date = datetime.strptime("2024-02-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-04-30", "%Y-%m-%d")

try:
    response = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["created_at", "author_id", "text", "lang"]
    )

    if response.data:
        for tweet in response.data:
            tweet_date = tweet.created_at
            tweet_author = tweet.author_id

            if tweet_author in excluded_authors:
                continue
            if not (start_date <= tweet_date <= end_date):
                continue

            print(f"Author ID: {tweet_author}")
            print(f"Tweet: {tweet.text}")
            print(f"Created At: {tweet_date}")
            print("-" * 50)

    else:
        print("No tweets found for the given query.")
        
except tweepy.TweepyException as e:
    print(f"An error occurred: {e}")