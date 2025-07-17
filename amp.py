import subprocess
import threading

channels = [
    (1, 0, "vocals.wav"),
    (2, 0, "drums.wav"),
    (3, 0, "bass.wav")
]

def play_stream(card, device, wav):
    cmd = ["aplay", "-D", f"hw:{card},{device}", wav]
    subprocess.run(cmd)

threads = []
for card, dev, wav in channels:
    t = threading.Thread(target=play_stream, args=(card, dev, wav))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All playback finished!")
