#!/usr/bin/python3
"""Reddit API query.
"""
import requests
import sys
headers = {
    'User-Agent': ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0"
                   "Safari/537.36")
}


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles of the first 10
        hot posts listed for a given subreddit.

       Args:
            subreddit (str): The subreddit.
    """
    url = "https://api.reddit.com/r/{}/hot.json?limit=10"
    url = url.format(subreddit)
    res = requests.get(url,
                       allow_redirects=False,
                       headers=headers)

    if res.status_code == 200:
        data = res.json().get('data')
        for post in data.get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
