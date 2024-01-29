#!/usr/bin/python3
"""Returns information about user TODO list progress"""
import sys
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    todos = requests.get(url + "users/" + sys.argv[1] + "/todos").json()
    user_id = sys.argv[1]
    username = user.get("username")
    with open(f"{user_id}.json", "w") as f:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, f)
