import configparser
from webbrowser import get
from .paths import CONFIG
Configuration = configparser.ConfigParser()
Configuration.read(CONFIG)

CLIENTID = Configuration['DEFAULT']['ClientId'] # Client ID of application, can be found in https://discordapp.com/developers/applications/
SHOW_TIME = Configuration['DEFAULT']['ShowTimestamp'] == 'True' # Show timestamp in discord
STATE = Configuration['DEFAULT']['State'] 
DETAILS = Configuration['DEFAULT']['Details']
LARGE_IMAGE = Configuration['DEFAULT']['LargeImage']
LARGE_TEXT = Configuration['DEFAULT']['LargeText']
SMALL_IMAGE = Configuration['DEFAULT']['SmallImage'] 
SMALL_TEXT = Configuration['DEFAULT']['SmallText']
# WIP

# if value has $variable in it, replace with variable
def replace(value, data):
    if '$' in value:
        value = value.replace('$heartRate', str(data))
    return value

#SHOW_CALORIES = config['DEFAULT']['ShowCalories']
#SHOW_MOTION = config['DEFAULT']['ShowMotion']
#SHOW_BASAL_ENERGY_BURNED = config['DEFAULT']['ShowBasalEnergyBurned']
