#!/usr/bin/python3
'''
A function that queries the Reddit API and returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Args:
        subreddit: Subreddit name

    Return:
          Number of total subscribers or 0
    '''
    headers = {'User-Agent': 'CustomAgent'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        respons = requests.get(url, headers=headers, allow_redirects=False)
        data = respons.json()

        if 'data' in data:
            return data['data']['subscribers']
        return 0
    except Exception:
        return 0
