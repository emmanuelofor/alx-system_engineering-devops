#!/usr/bin/python3
"""Retrieve the subscriber count from a specified Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Fetch the subscriber count for the provided subreddit."""
    
    # Construct the URL for the subreddit's "about" page
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Define headers for the request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Make the request, disabling redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # If the subreddit does not exist (404), return a count of 0
    if response.status_code == 404:
        return 0
    
    # Extract subscriber count from the JSON response
    results = response.json().get("data")
    return results.get("subscribers")
