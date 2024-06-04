#!/usr/bin/python3
"""
This module contains the function recurse, which retrieves the titles
of all hot posts on a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store hot post titles.
        after (str): The "after" parameter for pagination.
        count (int): The count of retrieved posts.

    Returns:
        list: A list of titles of hot posts.
        None: If the subreddit is invalid or an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None

        try:
            results = response.json().get("data", {})
        except ValueError:
            return None

        after = results.get("after")
        count += results.get("dist", 0)
        for child in results.get("children", []):
            hot_list.append(child.get("data", {}).get("title"))

        if after:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
