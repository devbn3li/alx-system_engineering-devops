#!/usr/bin/python3
"""Function to query the Reddit API and return the number of subscribers
for a given subreddit."""

import requests


def top_ten(subreddit):
    """Return the top 10 hot posts for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    data = response.json()

    if response.status_code == 200:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
