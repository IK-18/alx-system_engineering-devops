#!/usr/bin/python3
"""Queries the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Queries the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    users = res.json().get("data")
    return users.get("subscribers")
