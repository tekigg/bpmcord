class HeartBeat:
    def __init__(self, data):
        self.json = data
        self.heartRate = data[1]
        return self

class Motion:
    def __init__(self, data):
        self.json = data
        self.x = data[1][0]
        self.y = data[1][1]
        self.z = data[1][2]
        return self

class BasalEnergyBurned:
    def __init__(self, data):
        self.json = data
        self.EnergyBurned = data[1]
        return self

class Calories:
    def __init__(self, data):
        self.json = data
        self.calories = data[1]
        return self

def CheckDataType(data):
    data = data.split(":")
    if data[0] == "heartRate": return HeartBeat(data), "heartRate"
    elif data[0] == "motion": return Motion(data), "motion"
    elif data[0] == "basalEnergyBurned": return BasalEnergyBurned(data),  "basalEnergyBurned"
    elif data[0] == "calories": return Calories(data), "calories"
