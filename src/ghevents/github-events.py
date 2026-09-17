#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """Fetch JSON event data from the given GitHub API URL and return it as a Python object."""
    x = requests.get(url).text
    events = json.loads(x)
    return events


def print_events(events, n=5):
    """Print the first n events in the form 'type :: repo_name'."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """Print the configured GitHub user and URL, fetch events, and display them."""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()
