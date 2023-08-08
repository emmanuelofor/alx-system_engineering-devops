#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""

    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    hot_posts = data.get("children", [])

    for post in hot_posts:
        title = post.get("data", {}).get("title", "")
        split_words = title.lower().split(' ')

        for word in word_count.keys():
            word_count[word] += split_words.count(word)

    after = data.get("after")

    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        sorted_counts = sorted([(k, v) for k, v in word_count.items() if v != 0], key=lambda x: (-x[1], x[0]))
        for k, v in sorted_counts:
            print(f'{k}: {v}')
