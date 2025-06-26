import numpy as np
import wave
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq

def get_amp_freq(path, min_ampy=1000):
    sample_rate, data = wavfile.read(path)
    if len(data.shape) == 2:
        data = data.mean(axis=1)

    window_size = 1024
    hop_size = 512
    min_amp = min_ampy

    data = data / np.max(np.abs(data))
    freq_amp_pairs = []

    for start in range(0, len(data)-window_size, hop_size):
        window = data[start:start+window_size]
        windowed = window * np.hanning(len(window))
        spectrum = rfft(windowed)
        amplitudes = np.abs(spectrum)
        frequencies = rfftfreq(window_size, 1 / sample_rate)

        peak_index = np.argmax(amplitudes)
        peak_amp = amplitudes[peak_index]
        peak_freq = frequencies[peak_index]

        if peak_amp >= min_amp:
            freq_amp_pairs.append((round(peak_freq, 2), round(peak_amp, 2)))
    print(freq_amp_pairs[:100])





if __name__ == "__main__":
    #visualize('venv/music/percussive.wav')
    get_amp_freq("venv/music/harmonic.wav")