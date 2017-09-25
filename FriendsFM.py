import pysrt
import os
import glob
import re
import pydub
from pydub import AudioSegment
from pysrt import SubRipFile
from pysrt import SubRipItem
from pysrt import SubRipTime
from PyLyrics import *

pydub.AudioSegment.converter = r"D://FFmpeg/bin/ffmpeg.exe"

# book = {}
# book['kb'] = {
# 	'name': 'tom',
# 	'address': '123 Springfield',
# 	'phone': 1234567890
# }

# book['sam'] = {
# 	'name': 'sam',
# 	'address': '124 Springfield',
# 	'phone': 5392849034
# }

# import json
# s=json.dumps(book)

i = 0
j = False
k = 0
Artist = 'Survivor'
Song = 'Eye of the Tiger'
filename = ''
lyrics = (PyLyrics.getLyrics(Artist,Song))
combinedAudio = AudioSegment.empty()
firstVisitedFlag = True

data = lyrics.split()
lyricsLen = len(data)
print("\n")

# Removing punctuation symbols from song lyrics so it would match with the subtitles
for i in range(lyricsLen):
	data[i] = re.sub(r'[^\w\s]','',data[i])

print(data)
print("\n")

subs_path = 'D://Users/Kabir/FriendsFM/Friends_Subs/'
video_path = 'D://Users/Kabir/MyVideos/FriendsSeason1-10COMPLETE720pBrRipx264[PAHE.in]/'
audio_path = 'D://Users/Kabir/MyVideos/FriendsSeason1-10COMPLETE720pBrRipx264[PAHE.in]/FriendsAudio/mp3'
export_path = 'D://Users/Kabir/FriendsFM/Friends_Audio/'

fnames = os.listdir(subs_path)
fnamesLen = len(fnames)

# In case the word is not found I replaced the audio with "something"
# subs = pysrt.open(subs_path + 'Friends.S01E01.720p.BluRay.x264-PSYCHD.srt')
# somethingAudio = AudioSegment.from_mp3(audio_path + '/Friends.S01E01.720p.BluRay.x264-PSYCHD.mp3')
# t1 = subs[2].start.seconds * 1000 + subs[2].start.milliseconds
# t2 = subs[2].end.seconds * 1000 + subs[2].end.milliseconds
# somethingAudio = somethingAudio[t1:t2]
# somethingAudio.export(export_path + 'something.mp3', format='mp3')

#Searching through every srt file and matching each word from the lyrics of the song to the word in the srt file
for i, item in enumerate(data):
	firstVisitedFile = ''
	while k < fnamesLen:
		# If I went through all the files and couldn't find matching subs
		if (firstVisitedFile == fnames[k]) and (firstVisitedFlag == False):
			firstVisitedFlag = True
			print(data[i])
			print("NOT FOUND")
			# combinedAudio = combinedAudio + somethingAudio
			break
		if firstVisitedFlag:
			firstVisitedFile = fnames[k]
			firstVisitedFlag = False
		subs = pysrt.open(subs_path + fnames[k])
		# Looking for first matching sub
		for part in subs:
			searchSub = re.search(r'\b' + data[i] + r'\b', part.text, re.IGNORECASE)
			if searchSub:
				print("\n")
				print(data[i])
				print(part.text)
				j = True
				firstVisitedFlag = True
				# Finds the part of the subs in which the word is being said and exports it as a new audio file for Google Speech Api
				filename = fnames[k]
				mp3_filename = filename[0:38] + '.mp3'
				newAudio = AudioSegment.from_mp3(audio_path + '/' + mp3_filename)
				t1 = part.start.minutes * 60 * 1000 + part.start.seconds * 1000 + part.start.milliseconds
				t2 = part.end.minutes * 60 * 1000 + part.end.seconds * 1000 + part.end.milliseconds
				newAudio = newAudio[t1:t2]
				combinedAudio = combinedAudio + newAudio
				break
		if k == fnamesLen - 1:
			k = 0
		else:
			k += 1

		if j:
			j = False
			break

combinedAudio.export(export_path + 'combined.mp3', format='mp3')



	
