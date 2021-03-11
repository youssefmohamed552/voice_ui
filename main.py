# import zipfile
from recorder import Recorder
from stt import SpeechToText
from tts import TextToSpeech



def main():
  recorder = Recorder()
  stt = SpeechToText()
  tts = TextToSpeech()
  recorder.run()
  out = stt.convert('speech_orig.wav')
  print('response: ', out)
  tts.say('you just said ' +  out)



if __name__ == '__main__':
  main()

