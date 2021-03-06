#!/usr/bin/python3
""" export data in the CSV format """
import csv
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
            [sys.argv[1],
             username,
             item.get("completed"),
             item.get("title")]
        )

    with open(sys.argv[1] + ".cvs", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for row in listed_items:
            writer.writerow(row)
