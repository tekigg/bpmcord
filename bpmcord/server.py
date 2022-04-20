from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from .utils import exceptions, Log
from .animate import *
from .utils.objects import *

animation = Animate()
class ws(WebSocket):
    def handleMessage(self):
        Log(1, self.data)
        try:
            obj = CheckDataType(self.data)
            if obj.heartRate:
                animation.heartRate = obj.heartRate
                animation.animate()
        except Exception as e:
            pass
            #print(e)


    def handleConnected(self):
        Log(1, "Client connected successfully.")

    def handleClose(self):
        Log(3, "Client disconnected from the server.")
        raise exceptions.WatchDisconnected(self.data)

    def stop(self):
        self.close()

