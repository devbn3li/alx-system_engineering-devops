#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos", params={"userId": user_id}).json()
    completed = [task for task in todo if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for task in completed:
        print("\t {}".format(task.get("title")))
