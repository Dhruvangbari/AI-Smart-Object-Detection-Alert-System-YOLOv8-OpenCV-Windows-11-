import threading
from playsound import playsound
import datetime
import os

def play_alarm(sound_path):
    def sound():
        playsound(sound_path)
    threading.Thread(target=sound, daemon=True).start()

def log_detection(label):
    os.makedirs("logs", exist_ok=True)
    with open("logs/detections.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {label}\n")
