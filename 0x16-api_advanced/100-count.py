#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after=None, word_dict=None):
    """ A function that queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """

    if word_dict is None:
        word_dict = {}

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title'].lower()

            for word in word_list:
                if title.count(word.lower()):
                    if word.lower() in word_dict:
                        word_dict[word.lower()] += title.count(word.lower())
                    else:
                        word_dict[word.lower()] = title.count(word.lower())

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        sys.exit(1)
    subreddit = sys.argv[1]
    word_list = [word.lower() for word in sys.argv[2:]]
    count_words(subreddit, word_list)
