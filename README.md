# VOICE USER INTERFACE

## INSTALL

### prerequesits
on ubuntu system `sudo apt-get install libportaudio2 libespeak1 python3.8-venv -y`
- `portaudio` nessecary for using `torchaudio`
- `libespeak1` nessecary for using `pyttsx3` -> does the speech to text conversion
- `python3.8-venv` nesscesary for creating a virtual environment 

### virtual environment 
- create a virtual environment `python3 -m venv env`
- activate the environment  `source env/bin/activate`

### required packages
- `pip install -r requirements.txt`
