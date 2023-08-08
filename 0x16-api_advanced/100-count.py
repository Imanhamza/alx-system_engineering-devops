#!/usr/bin/python3
'''
A recursive function that queries the Reddit API, parses the title of
all hot articles,and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
'''
import requests


def count_words(subreddit, word_list):
    '''
    Args:
        subreddit: Name of subreddit
        word_list: List of given keywords
    Return:
     list containing the titles of all hot articles
    '''
    headers = {'User-Agent': 'CustomAgent'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # parms = {'after' : after}

    try:
        response = requests.get(
                url, headers=headers, allow_redirects=False)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']

                for word in word_list:
                    word = word.lower()
                    count = title.lower().count(word)
                    if count > 0:
                        print(f"{word}\t{count}")
    except Exception:
        return None
