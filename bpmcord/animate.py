from bpmcord.utils.objects import HeartBeat
from .utils.config import CLIENTID, STATE, DETAILS, LARGE_IMAGE, LARGE_TEXT, SMALL_IMAGE, SMALL_TEXT, SHOW_TIME, replace
from pypresence import Presence
import time
RPC = Presence(str(CLIENTID))
RPC.connect() 

# time script had ran for
start = time.time()

class Animate():
    def __init__(self):
        self.heartRate = None
        self.motion = None
        self.basalEnergyBurned = None
        self.calories = None
        self.timestamp = None

    def animate(self):
        try:
            if SHOW_TIME:
                RPC.update(state=replace(STATE, self.heartRate), details=DETAILS, large_image=LARGE_IMAGE, large_text=LARGE_TEXT, small_image=SMALL_IMAGE, small_text=SMALL_TEXT, start=start)
            else:
                RPC.update(state=replace(STATE, self.heartRate), details=DETAILS, large_image=LARGE_IMAGE, large_text=LARGE_TEXT, small_image=SMALL_IMAGE, small_text=SMALL_TEXT, start=None)
        except Exception as e:
            print(e)