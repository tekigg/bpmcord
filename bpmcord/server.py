from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from .utils import exceptions, Log

class ws(WebSocket):
    def handleMessage(self):
        Log(1, self.data)

    def handleConnected(self):
        Log(1, "Client connected successfully.")

    def handleClose(self):
        Log(3, "Client disconnected from the server.")
        raise exceptions.WatchDisconnected(self.data)

    def stop(self):
        self.close()

