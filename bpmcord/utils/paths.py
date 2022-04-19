from genericpath import exists
import winshell
import os
from pathlib import Path

MANAGED = os.path.join(winshell.my_documents(), "bpmcord") # Origin documents path
LOGS_THREAD_MAIN = fr"{MANAGED}\logs\main.thread.log.txt" # Main thread logs file
FAVICON = r"bpmcord\utils\assets\favicon.ico" # Tray icon

if not exists(MANAGED): os.makedirs(MANAGED+'\logs') #WORK FFS

