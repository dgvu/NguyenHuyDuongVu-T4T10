from __future__ import unicode_literals

from youtube_dl import YoutubeDL
import youtube_dl
import json
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('that girl', False)

song_url = search_result['entries'][1]['webpage_url']

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([song_url])

# # as requested in comment
# exDict = {'exDict': search_result}

# with open('file.txt', 'w') as file:
#      file.write(json.dumps(search_result)) # use `json.loads` to do the reverse

