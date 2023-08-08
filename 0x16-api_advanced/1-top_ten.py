#!/usr/bin/python3
'''
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''
    Args:
        subreddit: Subreddit name

    Return:
          10 hot posts
    '''
    headers = {'User-Agent': 'CustomAgent'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    parms = {'limit': 10}

    try:
        respons = requests.get(
                url, headers=headers, allow_redirects=False, params=parms)
        data = respons.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        print('None')
    except Exception:
        print('None')
