#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list containing the titles of all
    hot articles for a given subreddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None
    posts = res.json().get("data")
    after = posts.get("after")
    count += posts.get("dist")
    for post in posts.get("children"):
        hot_list.append(post.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
