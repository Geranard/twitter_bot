import tweepy
import threading
import datetime as dt
import time
import os

API_key = os.environ.get("API_KEY_TWITTER")
API_secret_key = os.environ.get("API_SECRET_KEY_TWITTER")
access_token = os.environ.get("ACCESS_TOKEN_TWITTER")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_TWITTER")

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

target_year = 2022

def tweet(year, month, day):
    global target_year
    dt1 = dt.date(year, month, day)
    dt2 = dt.date(target_year, 4, 20)
    delta = dt2 - dt1
    delta = delta.days

    message = ""

    if delta != 0:
        message = f"{delta} days until 04-20-{target_year}."

    else:
        message = f"It is 04-20-{target_year}."
        target_year += 1

    update_status = api.update_status(
        status=message
    )
    print(update_status)

def main():
    while True:
        now = dt.datetime.now()
        if now.hour==12 and now.minute==0 and now.second==0:
            tweet(now.year, now.month, now.day)
        time.sleep(1)

task = threading.Thread(target=main)
task.daemon = True
task.run()
