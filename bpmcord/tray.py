from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image

from .utils.paths import FAVICON
class Tray:
    def __init__(self, menu=None):
        self.menu = menu
        self.icon = icon("BPMCORD", Image.open(FAVICON), menu=menu)
        self.icon.run_detached()
    
    def exit(self):
        self.icon.stop()
        
        exit()



