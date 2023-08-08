#!/usr/bin/python3
'''
A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles
'''
import requests


def recurse(subreddit, hot_list=[]):
    '''
    Args:
        subreddit: Name of subreddit
        hot_list: List of hos posts
    Return:
     list containing the titles of all hot articles
    '''
    headers = {'User-Agent': 'CustomAgent'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list)
            return hot_list
    except Exception:
        return None
