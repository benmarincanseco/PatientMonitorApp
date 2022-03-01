import device


def testNoValidFile():
    actual = device.validateData("")
    expected = ["Invalid file"]
    assert actual == expected


def testInvalidID1():
    actual = device.validateData("invalidID1")
    expected = []
    assert actual == expected
