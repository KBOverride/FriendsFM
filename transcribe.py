# Uses Google Speech Api and makes a request
# Transcribes audio file and searches for the keyword(lyric)
# Returns start and end time of the keyword(lyric)
import io
import re
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe_file(speech_file, lyric, index):
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=48000,
        language_code='en-US',
        enable_word_time_offsets=True)

    response = client.recognize(config, audio)

    for result in response.results:
        alternative = result.alternatives[0]
        print('Transcript: {}'.format(alternative.transcript))
        print('Confidence: {}'.format(alternative.confidence))

        for word_info in alternative.words:
            word_info.word = re.sub(r'[^\w\s]','',word_info.word)
            word = word_info.word
            if(word.lower() == lyric[index].lower()):
              start_time = word_info.start_time
              end_time = word_info.end_time
              print('Word: {}, start_time: {}, end_time: {}'.format(
                  word,
                  start_time.seconds + start_time.nanos * 1e-9,
                  end_time.seconds + end_time.nanos * 1e-9))
              return word_info
              break
        return word_info