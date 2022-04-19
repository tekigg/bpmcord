from bpmcord.utils.objects import HeartBeat
from .utils.config import CLIENTID, FRAMES, SPEED
from pypresence import Presence
import time
import asyncio
from multiprocessing import Pool

RPC = Presence(str(CLIENTID))
RPC.connect() 
# time script had ran for
start = time.time()

class Animate(HeartBeat):
    def __init__(self):
        self.heartRate = HeartBeat
        self.motion = None
        self.basalEnergyBurned = None
        self.calories = None
        self.timestamp = None

    def animate(self, heartRate=None, motion=None, basalEnergyBurned=None, calories=None, timestamp=None):
        print("UPDATING STATUS")
        for i in range(FRAMES+1):
            time.sleep(SPEED)
            RPC.update(state="BPMCORD", details="BPMCORD", large_image=str(i+1), large_text=heartRate, small_image="bpmcord", small_text="BPMCORD", start=start)
