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


def testMultipleErrors():
    actual = device.validateData("deviceTestFiles/multiError")
    expected = "[<ValidationError: '-100 is less than the minimum of 1'>, "\
               "<ValidationError: \"2 is not one of ['Temperature', 'Blood Pressure', "\
               "'Pulse', 'Oximeter', 'Weight', 'Glucometer']\">,"\
               " <ValidationError: \"'Train' is not of type 'integer'\">, "\
               "<ValidationError: \"None is not of type 'number'\">]"
    assert actual == expected
