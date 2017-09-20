import pysrt
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

subs = pysrt.open('D://Users/Kabir/Python_Projects/Friends.S01E01.720p.BluRay.x264-PSYCHD.srt')


# printing the subs
i = 0
while i < len(subs):
	test_sub = subs[i]
	# print(subs.text)
	i +=1

#print(test_sub.start.minutes,":",test_sub.start.seconds)
#print(test_sub.start.seconds)
#print(test_sub.start.milliseconds)

#print(test_sub.end.minutes)
#print(test_sub.end.seconds)
#print(test_sub.end.milliseconds)

words = (PyLyrics.getLyrics('Michael Jackson','Billie Jean'))

data = words.split()

print(data[0])