#import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq

def get_amp_freq(path, window_size=1024, hop_size=512):
    sample_rate, data = wavfile.read(path)
    if len(data.shape) == 2:
        data = data.mean(axis=1)

    frequencies = []
    amplitudes = []

    for start in range(0, len(data)-window_size, hop_size):
        window = data[start:start+window_size]
        windowed = window * np.hanning(len(window))
        spectrum = rfft(windowed)

        freqs = rfftfreq(window_size, 1 / sample_rate)
        amps = np.abs(spectrum)

        peak_index = np.argmax(amps)

        frequencies.append(freqs[peak_index])
        amplitudes.append(amps[peak_index])

    print(amplitudes[:100])
    print(frequencies[:100])
'''
def listOfFreq(path):
    samplerate, data = wavfile.read(path);
    if data.ndim > 1:
        data = data.mean(axis = 1)

    fft_output = np.fft.fft(data)
    frequencies = np.fft.fftfreq(len(data), d=1/samplerate)

    magnitude = np.abs(fft_output)

    positive_frequencies_indices = np.where(frequencies >= 0)
    positive_frequencies = frequencies[positive_frequencies_indices]
    positive_magnitude = magnitude[positive_frequencies_indices]

    print(positive_frequencies[:100])
    print(positive_magnitude)
'''

def visualize(path):
    raw = wave.open(path)

    #read all frames of wav
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")

    frames = raw.getframerate()

    time = np.linspace(0, len(signal)/frames, num=len(signal))

    plt.figure(1)
    plt.title("Analyzing Wav")
    plt.xlabel("Time")
    plt.plot(time, signal)
    plt.show()



if __name__ == "__main__":
    #visualize('venv/music/percussive.wav')
    get_amp_freq("song.wav")