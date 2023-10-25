def isLeapYear(number):
    if (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0):
        print(str(number) + " er et skuddår")
        return True
    else:
        print(str(number) + " er ikke et skuddår")
        return False