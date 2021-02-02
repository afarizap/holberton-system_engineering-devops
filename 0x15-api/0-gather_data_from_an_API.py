#!/usr/bin/python3
""" using this REST API"""
import requests
import sys


if __name__ == "__main__":
    host = "https://jsonplaceholder.typicode.com/"
    path = "users/" + sys.argv[1]

    json_response = requests.get(host + path).json()
    print("Employee {} is done with tasks"
          .format(json_response.get('name')), end="")

    query = "todos?userId=" + sys.argv[1]
    json_response = requests.get(host + query).json()

    done_tasks = []
    for task in json_response:
        if task.get("completed") is True:
            done_tasks.append(task)

    print("({}/{}):".format(len(done_tasks), len(json_response)))
    for task in done_tasks:
        print("\x09\x20{}".format(task.get("title")))
