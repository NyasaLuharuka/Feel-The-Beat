import librosa
import librosa.display
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import audio


song_name = "tswift"
file = f'venv/music/{song_name}.wav'

audio_array, sr = librosa.load(file)



harmonic, percussive = librosa.effects.hpss(audio_array)

sf.write('venv/music/harmonic.wav', harmonic, sr)
sf.write('venv/music/percussive.wav', percussive, sr)

#uses waveplot
librosa.display.waveshow(audio_array, sr)
plt.savefig("venv/music/output.jpg")

# create new directories for each song
# start graphing each audio file by frequencies
