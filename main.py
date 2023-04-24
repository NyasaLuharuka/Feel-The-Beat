import librosa
import soundfile as sf

file = 'rickroll.wav'
audio_array, sr = librosa.load(file)

#harmonic, percussive = librosa.effects.hpss(audio_array)

#sf.write('harmonic.wav', harmonic, sr)
#sf.write('percussive.wav', percussive, sr)

count = 0
for sr in audio_array:
    count+=1
print(count)