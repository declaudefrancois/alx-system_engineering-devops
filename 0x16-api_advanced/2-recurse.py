#!/usr/bin/python3
"""Reddit API query.
"""
import requests
import sys
headers = {
    'User-Agent': ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0)"
                   "Gecko/20100101 Firefox/116.0"),
}


def recurse(subreddit, hot_list=[]):
    """ Queries the Reddit API and returns a list containing
        the titles of all hot articles for a given subreddit.

        Args:
            subreddit (str): The subreddit.
            hot_list (list): A list keeping track of all subreddit's
                             title.
    """
    url = "https://api.reddit.com/r/{}/hot.json{}"
    count = len(hot_list)
    last_post = hot_list[-1].get('data') if count > 0 else None
    after = last_post.get('name', '') if count > 0 else ''
    after = '?after={}'.format(after) if after != '' else ''

    res = requests.get(url.format(subreddit, after),
                       allow_redirects=False,
                       headers=headers)
    if res.status_code == 200:
        data = res.json().get('data')
        hot_list += data.get('children', [])
        if data.get('after'):
            return recurse(subreddit, hot_list)
        return [post.get('data').get('title') for post in hot_list]
    return []
