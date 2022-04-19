from bpmcord.utils.config import CLIENTID, FRAMES, SPEED
from pypresence import Presence
import time


RPC = Presence(str(CLIENTID))
RPC.connect() 
# time script had ran for
start = time.time()


def animate(heartRate=None, motion=None, basalEnergyBurned=None, calories=None, timestamp=None):
    print("UPDATING STATUS")
    for i in range(int(24)):
        time.sleep(float(0.05))
        RPC.update(state=heartRate, details=heartRate, large_image=str(i+1), large_text=heartRate, small_image="1", small_text=heartRate, start=start)

while True:
    animate("72")