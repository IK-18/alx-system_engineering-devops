#!/usr/bin/python3
"""Returns information about user TODO list progress"""
import sys
import requests
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    todos = requests.get(url + "users/" + sys.argv[1] + "/todos").json()
    user_id = sys.argv[1]
    username = user.get("username")
    with open(f"{user_id}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")])
            for t in todos]
