#!/usr/bin/python3
"""Reddit API.
"""
import requests
headers = {
    'User-Agent': ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0)"
                   "Gecko/20100101 Firefox/116.0"),
}


def count_words(subreddit, word_list, counts={}, after=""):
    """ Queries the Reddit API, parses the title of all hot articles, and
        prints a sorted count of given keywords.

        Args:
            subreddit(str): The subreddit to look in.
            word_list(list): The list of keyword.
            counts(dict): Occurence counts dictionary.
            after(str): The next page to fetch.
    """
    url = "https://api.reddit.com/r/{}/hot.json{}"
    after = '?after={}'.format(after) if after != '' else ''
    res = requests.get(url.format(subreddit, after),
                       allow_redirects=False,
                       headers=headers)

    if len(counts) == 0:
        for word in word_list:
            counts[word.lower()] = 0

    if res.status_code == 200:
        data = res.json().get('data')
        for post in data.get('children', []):
            postTitle = post.get('data').get('title')
            postTitle = postTitle.lower()
            for word in word_list:
                if word.lower() in postTitle:
                    wc = counts.get(word.lower())
                    counts[word.lower()] = wc + postTitle.count(word.lower())

        if data.get('after'):
            return count_words(subreddit, word_list,
                               counts, data.get('after'))

    sorted_counts = sorted(counts.items(), key=lambda x: x[1],
                           reverse=True)
    for count in sorted_counts:
        if count[1] > 0:
            print("{}: {}".format(count[0], count[1]))
