import json
import jsonschema
import os


def validateData(fileName):
    file =f ileName + ".json"
    with open('deviceSchema.json') as deviceSchema:
        schema = json.load(deviceSchema)
    validator = jsonschema.Draft7Validator(schema)
    if os.path.isfile(file) and os.access(file, os.R_OK):
        with open(file, 'r') as f:
            data = json.load(f)
        return list(validator.iter_errors(data))
    else:
        return ["Invalid file"]
