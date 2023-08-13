#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Get total subscriber of a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    """Change client's User-Agent string to something unique and descriptive
    as required by Reddit API terms"""
    headers.update({'User-Agent': 'Temz User Agent version 1.0'})
    r = requests.get(url, headers=headers).json()
    t_subscriber = r.get("data", {}).get("subscribers")

    if not t_subscriber:
        return 0
    else:
        return t_subscriber
