#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""
from email import header
import json
from urllib import request
import requests


def number_of_subscribers(subreddit):
    """
    Queries to Reddit API.
    """
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    resp = requests.get(URL, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    subs = resp.json()
    if 'data' not in subs:
        return 0
    if 'subscribers' not in subs.get('data'):
        return 0
    return resp.json()['data']['subscribers']