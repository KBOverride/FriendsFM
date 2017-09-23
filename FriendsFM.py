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

book = {}
book['kb'] = {
	'name': 'tom',
	'address': '123 Springfield',
	'phone': 1234567890
}

book['sam'] = {
	'name': 'sam',
	'address': '124 Springfield',
	'phone': 5392849034
}

import json
s=json.dumps(book)


#subs = pysrt.open('D://Users/Kabir/FriendsFM/Friends_Subs/Friends.S01E01.720p.BluRay.x264-PSYCHD.srt')


#printing the subs
# i = 0
# while i < len(subs):
# 	test_sub = subs[i]
# 	print(subs.index)
# 	i +=1

#for i in subs:
	#print(i.index)

#print(test_sub.start.minutes,":",test_sub.start.seconds)
#print(test_sub.start.seconds)
#print(test_sub.start.milliseconds)

#print(test_sub.end.minutes)
#print(test_sub.end.seconds)
#print(test_sub.end.milliseconds)


i = 0
j = False
Artist = 'Survivor'
Song = 'Eye of the Tiger'
lyrics = (PyLyrics.getLyrics(Artist,Song))
combinedAudio = AudioSegment.empty()

#print(lyrics)

data = lyrics.split()
lyricsLen = len(data)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print("\n")

for k in range(lyricsLen):
	data[k] = re.sub(r'[^\w\s]','',data[k])

print(data)
print("\n")

filename = ''

subs_path = 'D://Users/Kabir/FriendsFM/Friends_Subs/'
video_path = 'D://Users/Kabir/MyVideos/FriendsSeason1-10COMPLETE720pBrRipx264[PAHE.in]/'
audio_path = 'D://Users/Kabir/MyVideos/FriendsSeason1-10COMPLETE720pBrRipx264[PAHE.in]/FriendsAudio'
export_path = 'D://Users/Kabir/FriendsFM/Friends_Audio/'
season_path = 0

# Searching through every srt file and matching each word from the lyrics of the song to the word in the srt file
for i, item in enumerate(data):
	for filename in os.listdir(subs_path):
		subs = pysrt.open(subs_path + filename)
		#print(len(subs))
		for part in subs:
			searchObj = re.search(r'\b' + data[i] + r'\b', part.text, re.IGNORECASE)
			if searchObj:
				j = True
				print(part.text)
				print("\n")
				# Finds the part of the subs in which the word is being said and exports it as a new audio file for Google Speech Api
				mp3_filename = filename[0:38] + '.mp3'
				newAudio = AudioSegment.from_mp3(audio_path + '/' + mp3_filename)
				t1 = part.start.minutes * 60 * 1000 + part.start.seconds * 1000 + part.start.milliseconds
				t2 = part.end.minutes * 60 * 1000 + part.end.seconds * 1000 + part.end.milliseconds
				newAudio = newAudio[t1:t2]
				combinedAudio = combinedAudio + newAudio
				break
				# print(subs.text)
		if j:
			break
	if j == False:
		print(data[i])
	j = False

combinedAudio.export(export_path + 'combined.mp3', format='mp3')

	
