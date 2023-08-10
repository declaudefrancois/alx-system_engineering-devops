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


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
       (total subscribers) for a given subreddit.

       Args:
            subreddit (str): The subreddit.
       Returns:
            int: The numbers of subscribers. 0 If not a valid subreddit.
    """
    url = "https://api.reddit.com/r/{}/about.json"
    url = url.format(subreddit)
    res = requests.get(url,
                       allow_redirects=False,
                       headers=headers)

    if res.status_code == 200:
        data = res.json().get('data')
        return data.get('subscribers')
    return 0
