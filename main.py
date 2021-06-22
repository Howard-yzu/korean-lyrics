# encoding: utf-8
"""
billboard korean chart->korean song->genius.com lyrics->translate and romania spell-> .txt file
"""
import lyricsgenius
import requests
import billboard
from korean_romanizer.romanizer import Romanizer


# 取得Token
def get_access_token():
	# API網址
	url = "https://api.genius.com/oauth/token"

	# 標頭
	headers = {
		"Content-Type": "application/x-www-form-urlencoded",
		"Host": "api.genius.com"
	}
	# 參數
	data = {
		"grant_type": "client_credentials",
		"client_id": "cEMF6qda2t06uAZ1waITjf8lXpK7pTZXLIuQ9WGm_1YhsNcLzNfH2AX0GSc_tTtP",
		"client_secret": "8M53s8HZaZhI09U_YfNIXRdubxj7ToGILwz44pN6BXuZOPeMH57w7dZzEOfjSwsrsPv2yOKuNPUyyPpvnneJuQ"
	}
	access_token = requests.post(url, headers=headers, data=data)
	return access_token.json()["access_token"]

def save_lyrics(lyrics,title,artist):
	name = title + '_' + artist
	file = open("%s_lyrics.txt"%name, 'w', encoding="utf-8")
	file.write(lyrics)
	file.close()
def save_romanize_lyrics(lyrics,title,artist):
	name = title + '_' + artist
	file = open("%s_rom_lyrics.txt"%name, 'w', encoding="utf-8")
	file.write(lyrics)
	file.close()
	
# get genius.com access token
token = get_access_token()
genius = lyricsgenius.Genius(token)

#get chart from billboard korea-100
chart = billboard.ChartData('billboard-korea-100')
print(chart)


song_id = input("which song lyrics you want to download(enter the song id number):")
song_id = int(song_id) - 1
song = chart[song_id]
title = song.title
artist = song.artist

song = genius.search_song(title, artist)
lyrics = str(song.lyrics)
save_lyrics(lyrics,title,artist)

r = Romanizer(lyrics)
save_romanize_lyrics(r.romanize(),title,artist)

