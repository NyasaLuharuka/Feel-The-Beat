import subprocess
import threading

channels = [
    (2, 0, "vocals.wav"),
    (3, 0, "percussive.wav"),
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

print("Done")
