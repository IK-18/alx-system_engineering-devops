#!/usr/bin/python3
"""Returns information about user TODO list progress"""
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    todos = requests.get(url + "users/" + sys.argv[1] + "/todos").json()
    complete = [t.get("title") for t in todos if t.get("completed") is True]
    name = user.get("name")
    print(f'Employee {name} is done with tasks({len(complete)}/{len(todos)}):')
    [print(f'\t {task}') for task in complete]
