#!/usr/bin/python3
""" export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    host = "https://jsonplaceholder.typicode.com/"
    path = "users/" + sys.argv[1]

    username = requests.get(host + path).json().get("username")

    query = "todos?userId=" + sys.argv[1]
    tasks = requests.get(host + query).json()

    listed_items = []
    for item in tasks:
        listed_items.append(
            {'task': item.get('title'),
             'completed': item.get('completed'),
             'username': username,
             }
        )

    with open(sys.argv[1] + ".json", "w") as f:
        json.dump({str(sys.argv[1]): listed_items}, f)
