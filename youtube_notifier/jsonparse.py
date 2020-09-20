import json


def load_json(file):
    with open(file, 'r') as input:
        return json.load(input)

def save_json(data, filepath):
    with open(filepath, 'w') as output:
        json.dump(data, output, indent=4)

def parser(data):
    """ 'data' being the isolated json dict from yt channel page <script> tag """

    items = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']

    video_info = []
    for item in items:
        video_dict = {}
        video_dict['id'] = item['gridVideoRenderer']['videoId']
        video_dict['title'] = item['gridVideoRenderer']['title']['runs'][0]['text']
        try:
            video_dict['published'] = item['gridVideoRenderer']['publishedTimeText']['simpleText']
        except KeyError:
            video_dict['published'] = 'LIVE NOW'
        video_info.append(video_dict)
    
    return video_info
