print("       lirik buat cim")
import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.01):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)
 
def sing_song():
    lyrics = [ 
        ("marah marah mulu", 0.10),
        ("buang buang waktu", 0.10),
        ("mending nyanyi sama aku", 0.08),
        ("heeeeaaaaaahhhhh....", 0.17),
        ("engkollll :v", 0.06),
       
    ]
    delays = [0.07, 0.08, 0.09, 0.11, 0.12]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
if __name__ == "__main__":
    sing_song()
