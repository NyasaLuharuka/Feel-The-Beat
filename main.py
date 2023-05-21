import librosa
import librosa.display
import soundfile as sf
import numpy as np


song_name = "tswift"
file = f'venv/music/{song_name}.wav'

audio_array, sr = librosa.load(file)

S_full, phase = librosa.magphase(librosa.stft(audio_array))

S_filter = librosa.decompose.nn_filter(
    S_full,
    aggregate=np.median,
    metric='cosine',
    width=int(librosa.time_to_frames(2, sr=sr)))

S_filter = np.minimum(S_full, S_filter)

margin_i, margin_v = 2, 10
power = 2

mask_i = librosa.util.softmask(S_filter,
                               margin_i * (S_full - S_filter),
                               power=power)
mask_v = librosa.util.softmask(S_full - S_filter,
                               margin_v * S_filter,
                               power=power)

S_foreground = mask_v * S_full
S_background = mask_i * S_full

y_foreground = librosa.istft(S_foreground * phase)
sf.write('venv/music/vocal.wav', y_foreground, sr)



harmonic, percussive = librosa.effects.hpss(audio_array)

sf.write('venv/music/harmonic.wav', harmonic, sr)
sf.write('venv/music/percussive.wav', percussive, sr)
