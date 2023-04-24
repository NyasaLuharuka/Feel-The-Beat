import librosa
import soundfile as sf
import os

file = 'venv/music/rickroll.wav'
audio_array, sr = librosa.load(file)

harmonic, percussive = librosa.effects.hpss(audio_array)

sf.write('venv/music/harmonic.wav', harmonic, sr)
sf.write('venv/music/percussive.wav', percussive, sr)