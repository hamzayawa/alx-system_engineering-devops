#!/usr/bin/python3
"""
fxn that queries Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import json
import requests

def top_ten(subreddit):
    """Return the first 10 hot posts listed for a given subreddit."""
    URL = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Chrome/51.0.2704.103'}
    r = requests.get(URL, headers=headers)
    if r.status_code == 200:
        r = r.json()
        get = r.get('data').get('children')
        my_list = []
        for x in get:
            y = x.get("data")
            print(y.get("title"))
    else:
        print(None)
