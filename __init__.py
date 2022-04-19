
"""
BPMCORD - A python package for the BPMCORD project. 

Show your heart rate in real time on your discord status, no Health Data Server needed.
"""

state = False

from bpmcord.tray import *


def on_clicked(item):
    print("check")

Tray(menu(
    item(
        'Enable',
        on_clicked,
        checked=lambda item: state)))


from bpmcord import server