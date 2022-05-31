#!/usr/bin/python3
''' Write a Python script that queries the Reddit API '''

import requests


def number_of_subscribers(subreddit):
    ''' Return the number of subscribers of a subreddit '''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        return (0)
    request = request.json()

    if "data" in request:
        return (request.get("data").get("subscribers"))
    else:
        return (0)
