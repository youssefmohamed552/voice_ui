# import zipfile
from recorder import Recorder
from stt import SpeechToText
from tts import TextToSpeech
# from model import eval_sentence
#from dialogue import Dialogue
from qa_system import QA_system
from torchtext.datasets import WikiText2
from torchtext.data.utils import get_tokenizer
from googlesearch import search
from urllib3 import request 




def get_context():
  train_iter = WikiText2(split='valid')
  context = ''
  for i, line in enumerate(train_iter):
    if i > 20:
      break
    context += line + ' '
  return context



def respond(tts, qa, question, context, is_vocal):
  answer = qa.run(question, context)
  print('question: ', question)
  print('response: ', answer)
  if is_vocal:
    tts.say('the question was ' + question)
    tts.say('and the answer is ' + answer)

  


def browse_the_web(query):
  print('query: ', query)
  link = next(search(query, tld='co.in', num=1, stop=1, pause=2))
  print('response link: ', link)
  html = request('GET', link)
  print('html: ', html)




def main():
  # context = get_context()
  context = '''
    Homarus gammarus , known as the European lobster or common lobster , is a species of <unk> lobster from the eastern Atlantic Ocean , Mediterranean Sea and parts of the Black Sea . It is closely related to the American lobster , H. americanus . It may grow to a length of 60 cm ( 24 in ) and a mass of 6 kilograms ( 13 lb ) , and bears a conspicuous pair of claws . In life , the lobsters are blue , only becoming " lobster red " on cooking . Mating occurs in the summer , producing eggs which are carried by the females for up to a year before hatching into <unk> larvae . Homarus gammarus is a highly esteemed food , and is widely caught using lobster pots , mostly around the British Isles
    '''
  recorder = Recorder()
  stt = SpeechToText()
  tts = TextToSpeech()
  qa = QA_system()
  # dialogue = Dialogue()
  recorder.run()
  # question = stt.convert('speech_orig.wav')
  question = 'what is a square?'
  browse_the_web(question)
  # print(question)
  # answer = dialogue.eval(sentence)
  # answer = qa.run('What is the name of the repository ?', 'Pipeline have been included in the huggingface/transformers repository')
  # questions = [
    # 'what is Homarus gammarus', 
    # 'how big does the Homarus gommarus grow ?', 
    # 'how much does the Homarus gommarus weigh ?', 
    # 'what is the mating process for Homarus gommarus ? ', 
    # 'when is the mating process for Homarus gommarus ? '
  # ]
  # for question in questions:
    # respond(tts, qa, question, context, True)



if __name__ == '__main__':
  main()

