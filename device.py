import json
import jsonschema
import os


# Function to validate that the data that is inputed is in the proper format
def validateData(fileName):
    file = fileName + ".json"
    with open('deviceSchema.json') as deviceSchema:
        schema = json.load(deviceSchema)
    validator = jsonschema.Draft7Validator(schema)
    if os.path.isfile(file) and os.access(file, os.R_OK):
        with open(file, 'r') as f:
            data = json.load(f)
        return str(list(validator.iter_errors(data)))
    else:
        return str(["Invalid file"])


# Access specific Keys functions
# Get Device ID
def getDevID(jsonFile):
    return jsonFile['device_id']


# Get Device Type
def getDevType(jsonFile):
    return jsonFile['device_type']


# Get Target ID
def getTarID(jsonFile):
    return jsonFile['target_id']


# Get Specific Metric
def getValue(jsonFile):
    return jsonFile['value']


# Get Unit
def getUnit(jsonFile):

    accesor = getDevType(jsonFile)
    allowableUnits = {
        "Temperature": "F",
        "Blood Pressure": "mmHg",
        "Pulse": "BPM",
        "Oximeter": "%",
        "Weight": "lbs",
        "Glucometer": "mg/dL"
        }
    return allowableUnits[accesor]


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
