#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def add_item(hot_posts, hot_list):
    """
    Adds item into a list
    """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_item(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=''):
    """
    Queries to Reddit API
    """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {
        'User_Agent': 'Mozilla/5.0'
    }

    params = {
        'after': after
    }

    resp = requests.get(URL,
                        headers=headers,
                        params=params,
                        allow_redirects=False)
    if resp.status_code != 200:
        return None

    subs = resp.json()
    posts = subs['data']['children']
    add_item(hot_list, posts)
    after = subs['data']['children']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
