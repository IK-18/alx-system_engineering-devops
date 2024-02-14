#!/usr/bin/python3
"""
Prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Prints a sorted count of given keywords
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
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
    try:
        if res.status_code == 404:
            raise Exception
        posts = res.json().get("data")
    except Exception:
        print("")
        return
    after = posts.get("after")
    count += posts.get("dist")
    for post in posts.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            if word in word_list:
                word_count = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = word_count
                else:
                    instances[word] += word_count
    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{key}: {value}") for key, value in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
