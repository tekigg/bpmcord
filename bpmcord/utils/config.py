import configparser
from .paths import CONFIG
Configuration = configparser.ConfigParser()
Configuration.read(CONFIG)
print(Configuration)
CLIENTID = Configuration['DEFAULT']['ClientId'] # Client ID of application, can be found in https://discordapp.com/developers/applications/
FRAMES = Configuration['DEFAULT']['Frames'] # Number of frames to be used in animation, found in Rich Presence assets tab. 
SPEED = Configuration['DEFAULT']['Speed'] # Speed of animation, recommended to be between 0.5 to 1 seconds. DO NOT SPAM THE API.

print(CLIENTID)

# WIP

#SHOW_CALORIES = config['DEFAULT']['ShowCalories']
#SHOW_MOTION = config['DEFAULT']['ShowMotion']
#SHOW_BASAL_ENERGY_BURNED = config['DEFAULT']['ShowBasalEnergyBurned']
