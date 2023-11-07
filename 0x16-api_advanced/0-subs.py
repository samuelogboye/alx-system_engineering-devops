#!/usr/bin/python3
""" A Python script that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
import requests


def number_of_subscribers(subreddit):
    """ A function that returns the number of subscribers for a given
        subreddit.
        """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
