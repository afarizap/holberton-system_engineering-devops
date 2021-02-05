#!/usr/bin/python3
""" queries Reddit API and print first 10 hot posts """
import requests


def top_ten(subreddit):
    """ print first 10 hot posts from given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {'User-agent': "xd"}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        for item in response.json()["data"]["children"]:
            print(item["data"]["title"])
    else:
        print(None)
