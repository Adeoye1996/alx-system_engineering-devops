#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """ A function that queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise exception for bad response
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        for post in children:
            title = post.get('data', {}).get('title', '')
            lower_title_words = [word.lower() for word in title.split()]

            for word in word_dict.keys():
                word_dict[word] += lower_title_words.count(word)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    count_words(subreddit, word_list, after, word_dict)
