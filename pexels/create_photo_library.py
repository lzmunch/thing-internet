"""
This script makes it easier to get new sets of links to photos by streamlining
the process of making queries to the Pexels API and post-processing of the
results. The final result is output to 

SETUP INFO:
1. You will need to set the environment variable PEXELS_API_KEY
   to your Pexels API key.
2. Modify the WORKING_DIR variable to point to an existing folderf

Pexels API docs:
https://www.pexels.com/api/documentation/

Author:
Lauren Zhang
"""

import json
import os

# where files will be created and written/overwritten
# edit this for your workspace
WORKING_DIR = ""

# how many links do we want for each thing
NUM_LINKS = 20

def query_pexels_api(thing, out_json):
    """
    Make a query to Pexels API and output data to json file
    Args:
        thing (str)
        out_json(str): output path
    Returns:
        None
    """
    print(f'Outputting results for {thing} to: {out_json}')

    # avoid duplicate queries
    if os.path.exists(out_json):
        print(f'  JSON already exists. Skipping...')
        return

    pexels_api_key = os.environ['PEXELS_API_KEY']
    request_cmd = f'curl -H "Authorization: {pexels_api_key}" ' \
                  f'"https://api.pexels.com/v1/search?query={thing}&per_page={NUM_LINKS}" ' \
                  f'> {out_json}'
    # print(request_cmd)
    os.system(request_cmd)

    return None

def links_from_json(in_json):
    """
    Read json data from in_json and pull url links out
    Args:
        in_json (str): path to json to read
    Returns:
        list(str)
    """
    data_str = None
    with open(in_json, 'r', encoding='utf-8') as f:
        data_str = f.read()

    data = json.loads(data_str)
    links = []
    for entry in data['photos']:
        links.append(entry['src']['original'])

    # print(links)
    return links

def create_photo_library(thing_list):
    """
    For a list of things, get the links for each and combine into
    a single link dictionary. Write to txt file.

    Args:
        list(str): list of things
    Returns:
        dict:
            keys(str): things like "fish", "goat", etc.
            values(list(str)): list of links to photos of key
    """
    if not os.path.exists(WORKING_DIR):
        return None

    txt_path = os.path.join(WORKING_DIR, f'thing_links.txt')

    link_dict = {}
    for thing in thing_list:
        json_path = os.path.join(WORKING_DIR, f'{thing}.json')
        query_pexels_api(thing, json_path)
        link_dict[thing] = links_from_json(json_path)

    json_str = json.dumps(link_dict)

    # need to escape backslash because we will store entire dict in
    # a string on glitch.com
    json_str = json_str.replace('"', '\\"')

    print(f'Writing links dict to {txt_path}')
    with open(txt_path, 'w+', encoding='utf-8') as f:
        f.write(json_str)

    return link_dict

if __name__ == '__main__':
    create_photo_library(['goat', 'fish', 'worm', 'toaster', 'internet'])
    print('\ndone.')
