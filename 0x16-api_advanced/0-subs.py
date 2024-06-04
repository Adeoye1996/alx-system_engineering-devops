#!/usr/bin/python3
"""
Script that queries the number of subscribers of a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        return response.json().get('data', {}).get('subscribers', 0)
    except requests.RequestException:
        return 0
