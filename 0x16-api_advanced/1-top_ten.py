#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return the number of subscribers
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {
        'user_agent': 'Mozilla 5.0'
    }

    params = {
        'limit': 10
    }

    resp = requests.get(URL, headers=headers, params=params, allow_redirects=False)
    if resp.status_code != 200:
        print(None)
        return
    subs = resp.json()
    posts = subs['data']['children']
    if len(posts) == 0:
        print(None)
    else:
        for list_post in posts:
            print(list_post['data']['title'])