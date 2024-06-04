#!/usr/bin/python3
"""
Script to print the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json().get("data", {}).get("children", [])
        if not data:
            print("None")
            return
        for post in data:
            print(post.get("data", {}).get("title"))
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except ValueError:
        print("Invalid JSON response")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        top_ten(sys.argv[1])
    else:
        print("Usage: ./1-top_ten.py <subreddit>")
