#!/usr/bin/python3
"""Queries the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
	"""Queries the number of subscribers for a given subreddit"""
	url = f'https://www.reddit.com/r/{subreddit}/about.json'
	headers = {
		"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/effective-zone4090)"
	}
	res = requests.get(url, headers=headers, allow_redirects=False)
	if res.status_code == 404:
		return 0
	users = res.json().get("data")
	return users.get("subscribers")