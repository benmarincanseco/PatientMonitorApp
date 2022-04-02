import device


def testNoValidFile():
    actual = device.validateData("")
    expected = "['Invalid file']"
    assert actual == expected


def testInvalidID1():
    actual = device.validateData("deviceTestFiles/invalidID1")
    expected = "[<ValidationError: '-102 is less than the minimum of 1'>]"
    assert actual == expected


def testInvalidID2():
    actual = device.validateData("deviceTestFiles/invalidID2")
    expected = "[<ValidationError: \"'car' is not of type 'integer'\">]"
    assert actual == expected


def testInvalidType():
    actual = device.validateData("deviceTestFiles/invalidType")
    expected = "[<ValidationError: \"'RaceCar' is not one of ['Temperature',"\
               " 'Blood Pressure', 'Pulse', 'Oximeter', 'Weight', 'Glucometer']\">]"
    assert actual == expected


def testInvalidValue():
    actual = device.validateData("deviceTestFiles/invalidValue")
    expected = "[<ValidationError: \"'1' is not of type 'number'\">]"
    assert actual == expected


def testMissingTime():
    actual = device.validateData("deviceTestFiles/noHourMinute")
    expected = "[<ValidationError: \"None is not of type 'integer'\">,"\
               " <ValidationError: \"None is not of type 'integer'\">]"
    assert actual == expected


def testValid():
    actual = device.validateData("deviceTestFiles/valid")
    expected = "[]"
    assert actual == expected


def testValidDevID():
    actual = device.getDevID(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 315
    assert actual == expected


def testValidDevType():
    actual = device.getDevType(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 'Temperature'
    assert actual == expected


def testValidTargetID():
    actual = device.getTarID(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 465
    assert actual == expected


def testValidValue():
    actual = device.getValue(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 100
    assert actual == expected


def testValidUnit():
    actual = device.getUnit(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 'F'
    assert actual == expected


def testValidYear():
    actual = device.getYear(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 2042
    assert actual == expected


def testValidMonth():
    actual = device.getMonth(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 8
    assert actual == expected


def testValidDay():
    actual = device.getDay(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 26
    assert actual == expected


def testValidHour():
    actual = device.getHour(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 14
    assert actual == expected


def testValidMinute():
    actual = device.getMinute(device.convertFileToJson("deviceTestFiles/valid.json"))
    expected = 5
    assert actual == expected


def testMultipleErrors():
    actual = device.validateData("deviceTestFiles/multiError")
    expected = "[<ValidationError: '-100 is less than the minimum of 1'>, "\
               "<ValidationError: \"2 is not one of ['Temperature', 'Blood Pressure', "\
               "'Pulse', 'Oximeter', 'Weight', 'Glucometer']\">,"\
               " <ValidationError: \"'Train' is not of type 'integer'\">, "\
               "<ValidationError: \"None is not of type 'number'\">]"
    assert actual == expected
