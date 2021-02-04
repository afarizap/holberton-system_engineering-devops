#!/usr/bin/python3
""" queries Reddit API and returns number of subreddit subs """
import requests


def number_of_subscribers(subreddit):
    """ Retruns number of subscribers from a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-agent': "yolo"}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
