import sounddevice as sd
from scipy.io.wavfile import write

class Recorder:
  def __init__(self):
    self.fs = 44100
    self.seconds = 3

  def run(self):
    print('Recording ... ')
    self.myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
    sd.wait()  # Wait until recording is finished
    print('done recording thank you !! ')
    write('speech_orig.wav', self.fs, self.myrecording)  # Save as WAV file
