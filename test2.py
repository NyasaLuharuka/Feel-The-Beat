import subprocess

files = [
    ("test/venv/harmonic_mono.wav", "plughw:5,0"),
    ("test/venv/harmonic_mono.wav", "plughw:3,0"),
    ("test/venv/percussive_mono.wav", "plughw:2,0")
]

processes = []

for wav_file, device in files:
    cmd = ["aplay", "-D", device, wav_file]
    print("Playing")
    processes.append(subprocess.Popen(cmd))

for p in processes:
    p.wait()

print("Done")
