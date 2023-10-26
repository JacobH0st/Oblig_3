from leapyear import isLeapYear


def test_leapyear_devidable_by_four():
    assert isLeapYear(4) == True

def test_leapyear_not_devidable_by_four():
    assert isLeapYear(1) == False

def test_leapyear_devidable_by_four_not_hundred():
    assert isLeapYear(100) == False

def test_leapyear_devidable_by_fourhundred():
    assert isLeapYear(400) == True

def test_leapyear_devidable_by_hundred_not_fourhundred():
    assert isLeapYear(500) == False

def test_leapyear_2000():
    assert isLeapYear(2000) == True

def test_not_leapyear_1700_1800_1900():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False


