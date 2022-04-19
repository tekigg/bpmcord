from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from utils import exceptions, Log

class SimpleEcho(WebSocket):
    def handleMessage(self):
        Log(1, self.data)
    
    def handleConnected(self):
        Log(1, "Client connected successfully.")

    def handleClose(self):
        Log(3, "Client disconnected from the server.")
        raise exceptions.WatchDisconnected(self.data)

server = SimpleWebSocketServer('0.0.0.0', 3476, SimpleEcho)

Log(1, "--------------- BPMCORD SERVER STARTED ---------------")
server.serveforever()