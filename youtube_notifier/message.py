def markdown(string):
    s = string.replace('|', '\\|')
    s = s.replace('-', '\\-')
    s = s.replace('!', '\\!')
    s = s.replace("'", "\\'")
    s = s.replace('_', '\\_')
    s = s.replace('*', '\\*')
    s = s.replace('&', 'and')
    s = s.replace('.', '\\.')
    s = s.replace('#', '\\#')
    s = s.replace('+', '\\+')
    s = s.replace('(', '\\(')
    s = s.replace('[', '\\[')
    s = s.replace('{', '\\{')
    # below might not be needed
    s = s.replace(')', '\\)')
    s = s.replace(']', '\\]')
    s = s.replace('}', '\\}')
    return s


def channel_header(name):
    name = markdown(name)
    header = '\n\nRecent uploads by *' + name + '*:'
    return header


def channel_entry(videos, message_type):
    """ 'videos' being list of dict entries """
    def video_line(vid):
        title = markdown(vid['title'])
        watch_link = 'https://www.youtube.com/watch?v=' + vid['id']
        pub = vid['published']
        line = '\n+\\* [{}]({}) _posted {}_'.format(title, watch_link, pub)
        return line
    
    def grab_sample(vids):
        num = len(vids)
        s_line = str(num) + ' entries found, including:'
        e_1 = video_line(vids[0])
        e_3 = video_line(vids[-1])
        if num > 2:
            mid = num // 2
            e_2 = video_line(vids[mid])
            s_line += e_1 + e_2 + e_3
            return s_line
        elif num == 2:
            s_line += e_1 + e_3
        elif num ==1:
            s_line += e_1
            return s_line

    if message_type:
        entry = ''
        for video in videos:
            l = video_line(video)
            entry += l
        return entry
    else:
        entry = '\nNEW CATEGORY \\- '
        entry += grab_sample(videos)
        return entry


def s_concatenate(list_):
    str_out = ''
    for i in list_:
        str_out += i
    return str_out