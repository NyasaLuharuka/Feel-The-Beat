import librosa.display
import numpy as np

# load in music
audio_array, sr = librosa.load("venv/music/song.mp3")

# set time in parts of song
time = np.arange(0, len(audio_array)) / sr

# splits music into simpler sine wave frequencies
D = librosa.stft(audio_array)

# measures the phase angle, how fast freq changes
phase = np.angle(D)

# calculates the inst freq
inst_freq = np.diff(phase) / (2 * np.pi / D.shape[1])

# pads any values that stay the same
inst_freq = np.pad(inst_freq, (0, 1), mode='constant')

# converts inst freq to hertz
inst_freq_hz = (inst_freq * sr) / (2 * np.pi)

min = 0
max = 1000

current_min = np.min(inst_freq_hz)
current_max = np.max(inst_freq_hz)

scaled_freq = (inst_freq_hz - current_min) / (current_max - current_min) * (max - min) + min
print(scaled_freq)
