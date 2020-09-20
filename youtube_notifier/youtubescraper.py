from bs4 import BeautifulSoup
import requests
import json
import re


def scraper(yt_link):
    """ yt_link == url from channels.json """

    print('Downloading page: {}...'.format(yt_link), end='')  # DEBUG
    res = requests.get(yt_link)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, 'html.parser')

    f = soup.find('body', dir='ltr')
    scripts = f.find_all('script')
    video_grid = scripts[1]
    video_grid_str = str(video_grid.string)

    json_regex = re.compile("({.*?});")
    match = json_regex.search(video_grid_str)

    if match:
        j = match.group(1)
        output = json.loads(j)
        print('Done')  # DEBUG
        return output
    else:
        print('\nERROR: There was a problem searching the json data')

