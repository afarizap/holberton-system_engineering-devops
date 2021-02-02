#!/usr/bin/python3
""" export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    host = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(host).json()

    host = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(host).json()

    all_records = {}
    for user in users:
        new_record = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                new_record.append(task)
        all_records[user.get('id')] = new_record

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_records, f)
