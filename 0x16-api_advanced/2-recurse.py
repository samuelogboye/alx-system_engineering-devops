#!/usr/bin/python3
""" A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.
    """
import requests


after = None
def recurse(subreddit, hot_list=[]):
    """ A recursive function that returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {
              "after": after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    if after is None:
        return hot_list
    else:
        hot_list += [c.get("data").get("title")
                     for c in results.get("children")]
        return recurse(subreddit, hot_list, after)
