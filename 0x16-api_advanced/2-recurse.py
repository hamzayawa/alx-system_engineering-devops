#!/usr/bin/python3
"""
fxn that queries Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return the first 10 hot posts listed for a given subreddit."""
    if after is not "":
        URL = "https://www.reddit.com/r/{}/hot/.json?after={}".format(
            subreddit, after)
    else:
        URL = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/51.0.2704.103'}
    r = requests.get(URL, headers=headers)
    if r.status_code == 200:
        r = r.json()
        get = r.get('data').get('children')
        aft = r.get('data').get('after')
        for x in get:
            y = x.get("data").get("title")
            hot_list.append(y)
        if aft is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, aft)
    else:
        return None
