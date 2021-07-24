import torch
import torchaudio
from glob import glob
from utils import (read_audio, read_batch, split_into_batches, prepare_model_input, Decoder)

device = torch.device('cpu')

class SpeechToText:
  def __init__(self):
    modelname = 'en_v3_jit.model'
    self.model = torch.jit.load(modelname)
    self.decoder = Decoder(self.model.labels)

  def convert(self, filename):
    test_files = glob(filename)
    batches = split_into_batches(test_files, batch_size=10)
    input = prepare_model_input(read_batch(batches[0]),device=device)
    output = self.model(input)
    response = []
    for example in output:
      response.append(self.decoder(example.cpu()))

    return ' '.join(response)

