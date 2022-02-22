import device


def testTest():
    actual = device.validateData("")
    expected = ["Invalid file"]
    assert actual == expected
