# Introduction
korean lyrics是一個能從[《Billboard》K-Pop 100百大單曲榜](https://www.billboard.com/charts/billboard-korea-100)中抓取曲目並透過[Genius.com](https://genius.com/) 的API下載歌詞，並將其儲存兩份.txt文件，一份為原韓文歌詞，另一份為轉換為羅馬拼音後的歌詞，此project主要是希望喜愛韓文歌曲的人卻不懂韓文發音的人能更容易唱著他們所喜愛的歌曲
# Setup
Before using this package you'll need to sign up for a (free) account that authorizes access to the [Genius API](https://genius.com/api-clients). The Genius account provides a access_token that is required by the package.
# Build process
- Acitivity flow:
   - Get the billboard-chart -> searching the song in lyrics website -> save the lyrics ->  romanize korean lyrics -> translate lyrics -> save the lyrics in right format
- Planning phase:
   - Get the billboard API or search the module which can get  the chart
   - search the lyrics website's API
   - search the korean-romanize module
   - search the translate module
- Coding phase:
   - testing all the API and references code 
   - find out the translate API all require payment or very less usage(remove the translate function)
- Building Phase:
   - build the proccess through the acitivity flow
- Testing Phase:
   - assume the different sitution and then deal with the MESSAGE the [Genius API](https://genius.com/api-clients) send back
# installation
```
pip install lyricsgenius
```
```
pip install billboard.py
```
```
pip install korean_romanizer
```
# Details of the approach
import neccessary module
```python
import lyricsgenius
import requests
import billboard
from korean_romanizer.romanizer import Romanizer
```
access Genius API Token
```python
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
# get genius.com access token
token = get_access_token()
genius = lyricsgenius.Genius(token)
```
get chart from billboard korea-100
```
chart = billboard.ChartData('billboard-korea-100')
print(chart)
```

# Results
run main.py in compiler
```
billboard-korea-100 chart from 2021-06-19
-----------------------------------------
1. 'Butter' by BTS
2. 'Dun Dun Dance' by OH MY GIRL
3. 'Next Level' by aespa
...
100. 'I Knew I Love' by Jeon Mi Do
which song lyrics you want to download(enter the song id number):
```
searching song you choose in [Genius.com](https://genius.com/)
```
Searching for "song name you choose" by artist_id...
```


# References
[billboard-charts](https://github.com/guoguo12/billboard-charts)\
[LyricsGenius](https://github.com/johnwmillr/LyricsGenius)\
[korean-romanizer](https://github.com/osori/korean-romanizer)
