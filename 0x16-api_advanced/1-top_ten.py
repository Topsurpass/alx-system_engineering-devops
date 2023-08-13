#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of top 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    """Get header and change its client's User-Agent as required by
    Reddit API terms"""
    header = requests.utils.default_headers()
    header.update({"User-Agent": "Temz User Agent Version 1.0"})
    r = requests.get(url, headers=header).json()
    posts_arr = r.get("data", {}).get("children", [])

    if not posts_arr:
        print(None)
    else:
        for k in posts_arr:
            print(k.get("data", {}).get("title"), end="\n")
