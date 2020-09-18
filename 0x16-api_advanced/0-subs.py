#!/usr/bin/python3
"""
0-subs.py
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    base_url = "https://www.reddit.com/r"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                       " AppleWebKit/537.36 (KHTML, like Gecko)"
                       " Chrome/70.0.3538.77 Safari/537.36")
    }
    try:
        resp = requests.get(
            "{}/{}/about.json".format(base_url, subreddit),
            headers=headers,
            allow_redirects=False
        )
        resp.raise_for_status()
    except Exception:
        return 0
    else:
        subscribers = resp.json().get('data').get('subscribers')
        return subscribers
