#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """return all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    """Get header and change its client's User-Agent as required by Reddit
    API terms"""
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': "Temz User Agent Version 1.0"})

    """update url at each recursive call with parameter 'after'"""
    if after != "tmp":
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)

    # append top titles to hot_list
    posts_arr = r.json().get('data', {}).get('children', [])
    if not posts_arr:
        return None
    for e in posts_arr:
        hot_list.append(e.get('data').get('title'))

    # get next param "after" else nothing else to recurse
    after = r.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
