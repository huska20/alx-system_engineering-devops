#!/usr/bin/python3
""" Module for storing the count_words function. """
from requests import get

def count_words(subreddit, word_list, word_count={}, page_after=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    headers = {'User-Agent': 'HolbertonSchool'}

    word_list = [word.lower() for word in word_list]

    if not word_count:
        word_count = {word: 0 for word in word_list}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if page_after:
        url += f'?after={page_after}'

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        data = r.json()['data']
        for child in data['children']:
            title_words = child['data']['title'].lower().split()
            for word in title_words:
                if word in word_count:
                    word_count[word] += 1

        if data['after']:
            count_words(subreddit, word_list, word_count, data['after'])
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f'{word}: {count}')
