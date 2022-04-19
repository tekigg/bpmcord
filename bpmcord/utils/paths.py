from genericpath import exists
import winshell
import os

MANAGED = os.path.join(winshell.my_documents(), "bpmcord") # Origin documents path
LOGS_THREAD_MAIN = fr"{MANAGED}\logs\main.thread.log.txt" # Main thread logs file
FAVICON = r"bpmcord\utils\assets\favicon.ico" # Tray icon
CONFIG = fr"{MANAGED}\config.ini" # Config file

if not exists(MANAGED): os.makedirs(MANAGED+'\logs')  #WORK FFS
if not exists(CONFIG):
    with open(CONFIG, 'w+', encoding="utf-8") as f: f.write(f"""[DEFAULT]
ClientId = 966086356617019422
Frames = 24
Speed = 0.5"""); f.close()


