# FriendsFM
Takes song lyrics and makes the song using audio from the popular sitcom "Friends"

## Library and Frameworks
- pysrt (Subtitle Parser)
- PyLyrics (Retrives song lyrics from lyrics.wikia.com)
- pydub (Manipulating audio)
- Google Speech API

Audio Folder is not on GitHub due to file size limits

## Current Problems that Need Fixing
- FriendsFM only analyzes Season 1-7. Need to fix Season 8-10.
- Season 6 Episode 23 does not have subs
- Season 8 Episode 11 cannot be converted to audio (memory error or big file size)
- Season 9 Episode 10 cannot be converted to audio (memory error or big file size)
- Season 9 Episode 23 Episode 24 cannot be converted (memory error)

Current Runtime for "Eye of the Tiger" without taking audio to Google Speech API: **14 min 35 sec**
