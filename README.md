# VOICE USER INTERFACE

## INSTALL

### prerequesits
on ubuntu system `sudo apt-get install libportaudio2 libespeak1 python3.8-venv -y`
- `portaudio` nessecary for using `torchaudio` and `sounddevice`
- `libespeak1` nessecary for using `pyttsx3` -> does the speech to text conversion
- `python3.8-venv` nesscesary for creating a virtual environment 

The speech recognition model is `Silero Speech-To-Text Models`: `https://pytorch.org/hub/snakers4_silero-models_stt/`
the model used in this project is `en_v3_jit.model` this is the latest at the time of this project: `https://models.silero.ai/models/en/en_v3_jit.model`

to get the model simply use: `wget "https://models.silero.ai/models/en/en_v3_jit.model"`

### virtual environment 
- create a virtual environment `python3 -m venv env`
- activate the environment  `source env/bin/activate`

### required packages
- `pip install -r requirements.txt`
