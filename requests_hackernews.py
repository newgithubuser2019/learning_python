# import pprint
import sys
from operator import itemgetter

import requests

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("------------------------------------------------------------------------------------------------------------")
print("\nStatus code:", r.status_code)  # A status code of 200 indicates a successful response
r.raise_for_status()

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    # print(submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
for submission_dict in submission_dicts:
    print("\n-------------------------------------------------------------------")
    print("Title:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
