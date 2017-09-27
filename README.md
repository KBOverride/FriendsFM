# FriendsFM
Takes song lyrics and makes the song using audio from the popular sitcom "Friends"

## Library and Frameworks
- pysrt (Subtitle Parser)
- PyLyrics (Retrives song lyrics from lyrics.wikia.com)
- pydub (Manipulating audio)
- Google Speech API

Audio Folder is not on GitHub due to file size limits

- Export transcribed data in JSON format so we don't have to waste credit for Google Cloud Services when transcribing for the same song again

## Current Problems that Need Fixing
- FriendsFM only analyzes Season 1-7. Need to fix Season 8-10.
- Season 6 Episode 23 does not have subs
- Season 8 Episode 11 cannot be converted to audio (memory error or big file size)
- Season 9 Episode 10 cannot be converted to audio (memory error or big file size)
- Season 9 Episode 23 Episode 24 cannot be converted to audio (memory error)
- Season 10 Episode 17 Episode 18 cannot be converted to audio

Current Progress: Completed but may add words that are missing in audio format to future songs. Problems listed above still need fixing.
