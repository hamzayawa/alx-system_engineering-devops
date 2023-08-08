#!/usr/bin/python3
'''fxn that queries Reddit API and returns the number of subscribers.
'''

import json
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    URL = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/51.0.2704.103'}
    r = requests.get(URL, headers=headers)
    if r.status_code == 200:
        r = r.json()
        return r['data']['subscribers']
    else:
        return 0
