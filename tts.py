import pyttsx3

class TextToSpeech:
  def __init__(self):
    self.engine = pyttsx3.init()

  def say(self, sentence):
    self.engine.say(sentence)
    self.engine.runAndWait()

if __name__ == '__main__':
  tts = TextToSpeech()
  tts.say('I am finally alive')
