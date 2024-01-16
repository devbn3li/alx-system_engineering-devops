#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests
import time

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    while True:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 1))
            time.sleep(retry_after)
            continue
        if response.status_code != 200:
            return 0
        return response.json().get('data').get('subscribers')

if __name__ == "__main__":
    number_of_subscribers(subreddit)
