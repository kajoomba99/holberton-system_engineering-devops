#!/usr/bin/python3
"""
1-top_ten.py
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    """
    base_url = "https://www.reddit.com/r"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       " AppleWebKit/537.36 (KHTML, like Gecko)"
                       " Chrome/70.0.3538.77 Safari/537.36")
    }
    try:
        resp = requests.get(
            "{}/{}/hot.json?limit=10".format(base_url, subreddit),
            headers=headers,
            allow_redirects=False
        )
        resp.raise_for_status()
    except Exception:
        print(None)
    else:
        subscribers = resp.json().get('data').get('children')
        for element in subscribers:
            stickied = element['data']['title']
            print(stickied)
