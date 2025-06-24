import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy.io import wavfile
from scipy.fftpack import fft
import soundfile as sf
def get_amp_freq(path, window_size=1024, hop_size=512):
    sample_rate, data = wavfile.read(path)
    data1, sample_rate1 = sf.read(path)
    if len(data.shape) == 2:
        data = data.mean(axis=1)



    amplitudes = data.tolist()

    num_windows = (len(data) - window_size) // hop_size
    frequencies = []

    for i in range(num_windows):
        start = i*hop_size
        end = start+window_size
        window = data[start:end] * np.hanning(window_size)
        spectrum = np.abs(fft(window))[:window_size // 2]

        peak_index = np.argmax(spectrum)
        freq = peak_index * sample_rate / window_size
        frequencies.append(freq)

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
    get_amp_freq("tmp.wav")