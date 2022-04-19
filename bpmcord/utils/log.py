import coloredlogs, logging
import time

from .paths import LOGS_THREAD_MAIN

coloredlogs.install() # colors the logs because pretty
timestamp = time.time() # timestamp of script start

class Log:
    def __init__(self, urgency=None, message=""):
        self.urgency = urgency
        self.message = message
        self.loggingAdapter = logging.getLogger("websockets.server")
        if self.urgency == 1: self.urgency = logging.info, "INFO"
        elif self.urgency == 2: self.urgency = logging.warning, "WARNING"
        elif self.urgency == 3: self.urgency = logging.error, "ERROR"
        elif self.urgency == 4: self.urgency = logging.critical, "CRITICAL"
        else: self.urgency = logging.debug, "DEBUG"

        self.urgency[0](self.message)
        # save to logs file
        
        with open(LOGS_THREAD_MAIN, 'a+', encoding="utf-8") as f: f.write(f"{int(time.time() - timestamp)} | {self.urgency[1]}: {self.message}\n"); f.close()
