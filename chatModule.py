import json
# Messages are going be in json format
# Time getter functions
# Get Year
def getYear(jsonFile):
    return jsonFile['time']['year']


# Get Month
def getMonth(jsonFile):
    return jsonFile['time']['month']


# Get Day
def getDay(jsonFile):
    return jsonFile['time']['day']


# Get Hour
def getHour(jsonFile):
    return jsonFile['time']['hour']


# Get Minute
def getMinute(jsonFile):
    return jsonFile['time']['minute']


# Import JSON File Helper Function
def convertFileToJson(filePath):
    with open(filePath, 'r') as f:
        data = json.load(f)
    return data
# Access specific Keys functions
# Get Device ID
def getSender(jsonFile):
    return jsonFile['sender_id']


# Get Device Type
def getReceiver(jsonFile):
    return jsonFile['receiver_id']


# Get Target ID
def getMessage(jsonFile):
    return jsonFile['message']
