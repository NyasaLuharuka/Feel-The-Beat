import matplotlib.pyplot as plt
import numpy as np
import wave

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
    visualize('venv/music/percussive.wav')