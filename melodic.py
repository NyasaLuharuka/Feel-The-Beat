import numpy as np
import librosa
from scipy.fft import rfft, rfftfreq
from collections import defaultdict
import heapq

path = "file.mp3"
data, sr = librosa.load(path, sr=None, mono=True)

window_size=2048
hop_size=1024

frequency_amplitude_map = defaultdict(float)

for start in range(0, len(data) - window_size, hop_size):
    window = data[start:start + window_size]
    windowed = window * np.hanning(len(window))
    spectrum = rfft(windowed)
    amps = np.abs(spectrum)
    freqs = rfftfreq(window_size, d=1/sr)

    for freq, amp in zip(freqs, amps):
        frequency_amplitude_map[freq] += amp

# Get top 3 frequencies by total amplitude
top_3 = heapq.nlargest(3, frequency_amplitude_map.items(), key=lambda x: x[1])

top_frequencies = [round(freq, 2) for freq, _ in top_3]
top_amplitudes = [round(amp, 2) for _, amp in top_3]

print("Top 3 Frequencies:", top_frequencies)
print("Corresponding Amplitudes:", top_amplitudes)