import pysrt
import os
import glob
import re
from pysrt import SubRipFile
from pysrt import SubRipItem
from pysrt import SubRipTime
from PyLyrics import *

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


subs = pysrt.open('D://Users/Kabir/FriendsFM/Friends_Subs/Friends.S01E01.720p.BluRay.x264-PSYCHD.srt')


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
lyrics = (PyLyrics.getLyrics('Survivor','Eye of the Tiger'))

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

path = 'D://Users/Kabir/FriendsFM/Friends_Subs/'

# Searching through every srt file and matching each word from the lyrics of the song to the word in the srt file
for i, item in enumerate(data):
	for filename in os.listdir(path):
		subs = pysrt.open(path + filename)
		#print(len(subs))
		for part in subs:
			searchObj = re.search(r'\b' + data[i] + r'\b', part.text, re.IGNORECASE)
			if searchObj:
				j = True
				print(part.text)
				print("\n")
				break
				# print(subs.text)
		if j:
			break
	if j == False:
		print(data[i])
	j = False
	
