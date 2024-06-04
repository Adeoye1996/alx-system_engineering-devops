#!/usr/bin/python3
"""
This module contains the function top_ten.
"""

import requests
from sys import argv


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {"User-Agent": "MyAPI/0.0.1"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")
        if data is None:
            print(None)
            return

        for post in data.get("children"):
            print(post.get("data").get("title"))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) == 2:
        top_ten(argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")
