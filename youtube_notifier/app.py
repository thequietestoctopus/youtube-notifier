from exception import BadRequest
from channel import Channel
import youtubescraper
import jsonparse
import telegram
import message
import os


def run_app(data_dir):
    chan_fp = os.path.join(data_dir, 'channels.json')
    uploads_fp = os.path.join(data_dir, 'uploads.json')

    data = jsonparse.load_json(chan_fp)

    full_video_list = []  # probably needs to be changed
    full_uploads_dict = {}
    for key in data.keys():
        chan = Channel(key)

        grid_data = youtubescraper.scraper(chan.ytlink)
        vids = jsonparse.parser(grid_data)

        if chan.searchterms:
            sub_dict = {}
            m_elems = []
            for term in chan.searchterms:
                term_vids = chan.search_titles(vids, term)
                m_type = term_vids.pop(0)  
                if term_vids:
                    sub_dict[term] = term_vids[0]['id']
                    elem = message.channel_entry(term_vids, m_type)
                    m_elems.append(elem)
                else:
                    sub_dict[term] = chan.check_last_upload(term)
            if m_elems:
                m = message.s_concatenate(m_elems)
            else:
                m = None

        else:
            sub_dict = {}
            all_vids = chan.search_titles(vids)
            m_type = all_vids.pop(0)  
            m_elems = []
            if all_vids:
                sub_dict[chan.empty_search] = all_vids[0]['id']
                elem = message.channel_entry(all_vids, m_type)
                m_elems.append(elem)
            else:
                sub_dict[chan.empty_search] = chan.check_last_upload(chan.empty_search)
            if m_elems:
                m = m_elems.pop()
            else:
                m = None
        
        full_uploads_dict[chan.name] = sub_dict
        if m:
            com = message.channel_header(chan.name) + m
            full_video_list.append(com)


    if full_video_list:
        message_full = message.s_concatenate(full_video_list)
        try:
            res = telegram.telegram_bot_sendtext(message_full)
            if BadRequest.check_for_err(res):
                raise BadRequest(res)
            else:
                jsonparse.save_json(full_uploads_dict, uploads_fp)
        except BadRequest as e:
            print('\nERROR -- {}'.format(e))  # DEBUG
            print('      -- message contents:')  # DEBUG
            print(message_full)  # DEBUG


if __name__ == "__main__":
    run_app('./youtube_notifier/data')