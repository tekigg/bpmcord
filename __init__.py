
"""
BPMCORD - A python package for the BPMCORD project. 

Show your heart rate in real time on your discord status, no Health Data Server needed.
"""

from bpmcord.tray import *
from bpmcord.server import *

def on_clicked():
    server.close()
    tray.exit()

tray = Tray(menu=menu(item("Exit", on_clicked)))
server = SimpleWebSocketServer('0.0.0.0', 3476, ws)

try:
    Log(1, "--------------- BPMCORD SERVER STARTED ---------------")
    server.serveforever()
except Exception as e:
    Log(3, "--------------- BPMCORD SERVER UNABLE TO RUN ---------------\n{}".format(e))