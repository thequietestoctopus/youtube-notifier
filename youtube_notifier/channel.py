import jsonparse
import re


class Channel:

    channel_dir = './youtube_notifier/data/channels.json'
    last_upload_dir = './youtube_notifier/data/uploads.json'
    empty_search = 'AllVideos'

    def __init__(self, name):
        self.name = name
        self.ytlink = self.set_link()
        self.searchterms = self.set_searchterms()

    def set_link(self):
        channel_dict = jsonparse.load_json(self.channel_dir)
        url = channel_dict[self.name]['url']
        return url
    
    def set_searchterms(self):
        channel_dict = jsonparse.load_json(self.channel_dir)
        terms = channel_dict[self.name]['searchTerms']
        return terms
    
    def check_last_upload(self, searchterm):
        uploads = jsonparse.load_json(self.last_upload_dir)
        try:
            if searchterm in uploads[self.name]:
                return uploads[self.name][searchterm]
        except KeyError:
            return None

    def search_titles(self, video_dicts, searchterm=None):
        if searchterm:
            last = self.check_last_upload(searchterm)
            regex = re.compile(searchterm)
            term_results = []
            if last:
                term_results.insert(0, 1)
                for d in video_dicts:
                    match = regex.search(d['title'])
                    if match:
                        if d['id'] == last:
                            return term_results
                        else:
                            term_results.append(d)
            else:
                term_results.insert(0, 0)
                for d in video_dicts:
                    match = regex.search(d['title'])
                    if match:
                        term_results.append(d)
                return term_results
        else:
            last = self.check_last_upload(self.empty_search)
            empty_results = []
            if last:
                empty_results.insert(0, 1)
                for e in video_dicts:
                    if e['id'] == last:
                        return empty_results
                    else:
                        empty_results.append(e)
            else:
                empty_results.insert(0, 0)
                for e in video_dicts:
                    empty_results.append(e)
                return empty_results
