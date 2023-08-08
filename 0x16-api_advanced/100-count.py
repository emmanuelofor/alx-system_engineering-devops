#!/usr/bin/python3
"""Counts occurrences of keywords in hot posts of a specified Reddit subreddit."""
import requests

def count_words(subreddit, word_list, instances={}, after=None):

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        return
    
    data = response.json().get("data")
    after = data.get("after")
    
    for post in data.get("children"):
        title = post.get("data").get("title").lower().split()
        for word in word_list:
            occurrences = title.count(word.lower())
            instances[word] = instances.get(word, 0) + occurrences

    if after:
        count_words(subreddit, word_list, instances, after)
    else:
        sorted_words = sorted([(k, v) for k, v in instances.items() if v > 0], key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
