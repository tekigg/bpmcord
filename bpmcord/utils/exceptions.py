from .log import Log

class WatchDisconnected(Exception):
    """
    - **Message** : Client disconnected from the server.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)
        Log(3, "Client disconnected from the server.\n Details: " + str(args[0]))
        print("Client disconnected from the server.")