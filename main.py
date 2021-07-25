from recorder import Recorder
from stt import SpeechToText
from tts import TextToSpeech
from qa_system import QA_system
from torchtext.data.utils import get_tokenizer
from googlesearch import search
from bs4 import BeautifulSoup
import requests






def respond(tts, qa, question, context, is_vocal):
  answer = qa.run(question, context)
  print('response: ', answer)
  if is_vocal:
    tts.say(answer)

  


def browse_the_web(query):
  print('query: ', query)
  link = next(search(query, tld='co.in', num=1, stop=1, pause=2))
  print('response link: ', link)
  response = requests.get(link)
  html = response.text if response.status_code in range (200, 300) else f'The link failed to retrieve requested information and returned with status code :{response.status_code}'
  return html




def main():
  recorder = Recorder()
  stt = SpeechToText()
  tts = TextToSpeech()
  qa = QA_system()
  recorder.run()
  question = stt.convert('speech_orig.wav')
  html = browse_the_web(question)
  soup = BeautifulSoup(html, 'html.parser')
  text = soup.get_text()
  respond(tts, qa, question, text, True)



if __name__ == '__main__':
  main()

