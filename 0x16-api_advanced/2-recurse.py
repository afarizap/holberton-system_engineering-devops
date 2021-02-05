#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ return list with hot articles from subreddit """
    url = "https://www.reddit.com/r/{}/hot.json?after={}&limit=100"\
        .format(subreddit, after)
    header = {'User-agent': "asd"}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        after = response.json()["data"]["after"]
        for item in response.json()["data"]["children"]:
            hot_list.append(item["data"]["title"])
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
