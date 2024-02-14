#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
    params = {
            "limit": 10
            }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    posts = res.json().get("data").get("children")
    [print(post.get("data").get("title")) for post in posts[1:]]
