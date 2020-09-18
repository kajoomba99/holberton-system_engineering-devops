#!/usr/bin/python3
"""
1-top_ten.py
"""

import requests


def recurse(subreddit, hot_list=[], after_param=""):
    """
    returns a list containing the titles of all hot articles
    """
    base_url = "https://www.reddit.com/r"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       " AppleWebKit/537.36 (KHTML, like Gecko)"
                       " Chrome/70.0.3538.77 Safari/537.36")
    }
    try:
        resp = requests.get(
            "{}/{}/hot.json?limit=500".format(base_url, subreddit),
            headers=headers,
            params={'after': after_param},
            allow_redirects=False
        )
        resp.raise_for_status()
    except Exception:
        return None
    else:
        subscribers = resp.json().get('data').get('children')
        for element in subscribers:
            stickied = element['data']['title']
            hot_list.append(stickied)
        after = resp.json().get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
