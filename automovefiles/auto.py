from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
#pip install watchdog

import os 
import json
import time 


class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modifed(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = 'C:\Users\NOC-BITSNET\Desktop\automovefiles\myFolder'
folder_destination = 'C:\Users\NOC-BITSNET\Desktop\automovefiles\NOC'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, folder_destination, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
