# Author: Kabir Singh
# Project: FriendsFM
# Description: Takes song lyrics and makes the song using audio from the popular sitcom "Friends".
import io
import pysrt
import os
import glob
import re
import pydub

from pydub import AudioSegment
from pysrt import SubRipFile
from pysrt import SubRipItem
from pysrt import SubRipTime
from transcribe import transcribe_file
from PyLyrics import *

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

pydub.AudioSegment.converter = r"D://FFmpeg/bin/ffmpeg.exe"

i = 0
j = False
k = 0
# Example: Using "Eye of the Tiger" as an example for now
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
audio_path = 'D://Users/Kabir/MyVideos/FriendsSeason1-10COMPLETE720pBrRipx264[PAHE.in]/FriendsAudio/flac/'
export_path = 'D://Users/Kabir/FriendsFM/Friends_Audio/'
temp_path = 'D://Users/Kabir/FriendsFM/Friends_Audio/Temporary/'
songs_path = 'D://Users/Kabir/FriendsFM/Friends_Audio/Songs/'

fnames = os.listdir(subs_path)
fnamesLen = len(fnames)

#Searching through every srt file and matching each word from the lyrics of the song to the word in the srt file
for i, item in enumerate(data):
	firstVisitedFile = ''
	while k < fnamesLen:
		# If I went through all the files and couldn't find matching subs
		if (firstVisitedFile == fnames[k]) and (firstVisitedFlag == False):
			firstVisitedFlag = True
			print(data[i])
			print("NOT FOUND")
			break
		if firstVisitedFlag:
			firstVisitedFile = fnames[k]
			firstVisitedFlag = False
		subs = pysrt.open(subs_path + fnames[k])
		# Looking for first matching sub
		for part in subs:
			searchSub = re.search(r'\b' + data[i] + r'\b', part.text, re.IGNORECASE)
			if searchSub:
				filename = fnames[k]
				flac_filename = filename[0:38] + '.flac'
				newAudio = AudioSegment.from_file(audio_path + flac_filename)
				# Finds the part of the subs in which the word is being said and exports it as a new audio file for Google Speech Api
				t1 = part.start.minutes * 60 * 1000 + part.start.seconds * 1000 + part.start.milliseconds
				t2 = part.end.minutes * 60 * 1000 + part.end.seconds * 1000 + 1000 + part.end.milliseconds
				newAudio = newAudio[t1:t2]
				newAudio.export(temp_path + 'temporary' + str(i) + '.flac', format='flac', parameters=["-ac", "1"])

				word_info = transcribe_file(temp_path + 'temporary' + str(i) + '.flac', data, i)
				if(word_info is not None):
					print("\n")
					print(word_info.word)
					print(data[i])
					if (word_info.word.lower() == data[i].lower()):
						j = True
						firstVisitedFlag = True
						start_time = word_info.start_time
						end_time = word_info.end_time
						start_milliseconds = start_time.nanos * 1e-9
						end_milliseconds = end_time.nanos * 1e-9
						t1 = start_time.seconds * 1000 + start_milliseconds * 1000
						t2 = end_time.seconds * 1000 + end_milliseconds * 1000
						keywordAudio = AudioSegment.from_file(temp_path + 'temporary' + str(i) + '.flac')
						keywordAudio = keywordAudio[t1:t2]
						combinedAudio = combinedAudio + keywordAudio
						break
		if k == fnamesLen - 1:
			k = 0
		else:
			k += 1

		if j:
			j = False
			break

combinedAudio.export(export_path + Song + '.flac', format='flac', parameters=["-ac", "2"])
print("\n")
print("Finished Song")




	
