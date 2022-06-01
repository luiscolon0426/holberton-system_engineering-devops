#!/usr/bin/python3
""" Recursive function that queries the reddit api
 parses the title, and prints a sorted count """

import requests
import sys
after = None
dict_count = []


def count_words(subreddit, word_list):
    """parses title of hot articles, and prints sorted count """
    global after
    global dict_count
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=param)
