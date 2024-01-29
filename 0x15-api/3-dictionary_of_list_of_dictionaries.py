#!/usr/bin/python3
"""Returns information about user TODO list progress"""
import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": t.get("username")
            } for t in requests.get(url + f'todos/?userId={u.get("id")}')
                               .json()] for u in users}, f)
