import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\\Users\\Jorge A Rozo P\\Downloads"
to_dir = "C:\\Users\\Jorge A Rozo P\\Downloads\\Imagenes_Archivos"

dir_tree = {
    "Image_File": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_File": ['.mpg', '.mp2', '.mpeg', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
class FileMoveventHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = on.path.splitext(event.src_path)
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)
            
            if extension in value:

                file_name = os.path.basename(event.src_path)
                print("Descargando" + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                
                if os.path.exist(path2):
                    print("El directorio existe...")
                    print("Moviendo" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Creando directorio...")
                    os.makedirs(path2)
                    print("Moviendo" + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)
#Inicializar clase event handler
event_handler = FileMoveventHandler()

#Iniciar observer
observer = observers()

#Programar el observer
observer.schedule(event_handler, from_dir, recursive = true)

#Iniciar observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Ejecutando...")
except KeyboardInterrupt:
    print("Detenido")
    observer.stop()