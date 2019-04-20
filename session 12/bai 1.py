from __future__ import unicode_literals
from youtube_dl import YoutubeDL
from pyglet.media import Source, Player, load
import youtube_dl
import pyglet
import ast
import json
import os

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

value = []
thongtin = []
music = []
hotro = []
a = ["Show All songs", "Show detail of a song", "Play a song", "Search and download songs", "Exit"]
print("Hello this is TK music app")

with open("music.json", "r") as read_file:
    thongtin = json.load(read_file)

for i in range(len(thongtin)):
    bien = thongtin[i].keys()
    music.append(*bien)

for i in range(len(thongtin)):
    bien1 = thongtin[i].values()
    value.append(*bien1)

_round = True

while _round:
    print("Pick one of a options")
    for i in range(len(a)):
        print(i+1, ", ", a[i])
    x = int(input(">>> "))
    if x == 1:
        if music == []:
            print("Song list is empty")
        else:
            for i in range(len(music)):
                print(i + 1, ":", music[i])

    if x == 2:
        if music == []:
            print("Song list is empty")
        else:
            for i in range(len(music)):
                print(i + 1, ":", music[i])
            
            muon = int(input("Enter song number ? "))
            data_music_info = value[muon - 1]
            for i in data_music_info:
                print(i.upper(),":",data_music_info[i])

    if x == 3:
        if music == []:
            print("Song list is empty")
        else:
            for i in range(len(music)):
                print(i + 1, ":", music[i])
            
            e = int(input("Enter song number ? "))
            player = pyglet.media.Player()
            source = pyglet.media.load('{}.mp3'.format(value[e - 1]['TITLE'] + "-" + value[e - 1]['ID']))
            player.queue(source)
            play_disc = True
            player.play()
            while play_disc:
                choice = input('Enter playback option (play, pause, stop)')
                if choice == 'play':
                    player.play()
                elif choice == 'pause':
                    player.pause()
                elif choice == 'stop':
                    player.delete()
                    play_disc = False
                else:
                    print("Sorry, your command is Invalid")        

    if x == 4:
        search = input("Enter seach a song : ")
        array_music = []
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s','format': '137/best','logger': MyLogger(),'progress_hooks': [my_hook],})
        with ydl:
            result = ydl.extract_info(
                'https://www.youtube.com/results?search_query='+search,
                download=False # We just want to extract the info
            )

        # array_music = []
        if 'entries' in result:
            # Can be a playlist or a list of videos
            for i in range(5) :
                video0 = result['entries'][i]
                array_music.append(video0)
        else:
            # Just a video
            video = result

        for i in range(len(array_music)):
            print(str(i + 1) + ' : ' + array_music[i]['title'])
        
        b = input("Do you want to download (y ou n)")

        if b == "n":
            pass

        elif b == "y":
            c = int(input("Enter the song position you want download "))
            
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
            search_result = ydl.extract_info(search, False)
            song_url = search_result['entries'][c - 1]['webpage_url']

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([song_url])
            
            data = {
                search_result['entries'][c - 1]['alt_title'] : {
                    'CREATOR' : search_result['entries'][c - 1]['creator'],
                    'TITLE' : search_result['entries'][c - 1]['title'],
                    'DURATION' : search_result['entries'][c - 1]['duration'],
                    'ID' : search_result['entries'][c - 1]['webpage_url_basename']
                },
            }     
            music.append(search_result['entries'][c - 1]['alt_title'])
            hotro.append(data)

            with open("music.json", "w") as write_file:
                json.dump(hotro, write_file, indent= 4)

            print("Done")
            d = input("Do you want to play it (y ou n) ")

            if d == "y":
                player = pyglet.media.Player()
                source = pyglet.media.load('{}.mp3'.format(search_result['entries'][c - 1]['title'] + "-" + search_result['entries'][c - 1]['webpage_url_basename']))
                player.queue(source)
                play_disc = True
                player.play()
                while play_disc:
                    choice = input('Enter playback option (play, pause, stop)')
                    if choice == 'play':
                        player.play()
                    elif choice == 'pause':
                        player.pause()
                    elif choice == 'stop':
                        player.delete()
                        play_disc = False
                    else:
                        print("Sorry, your command is Invalid")                
            elif d == "n":
                pass

    if x == 5:
        _round = False
    else:
        pass