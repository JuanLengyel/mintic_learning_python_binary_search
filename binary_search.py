import math

def binarySearch(numberList, numberToFind, low, high):
    
    if (high < low):
        return False
    
    mid = int(math.floor((low + high) / 2))

    numberInIndex = numberList[mid]

    if (numberInIndex == numberToFind):
        return True
    elif (numberInIndex < numberToFind):
        return binarySearch(numberList, numberToFind, mid + 1, high)
    else:
        return binarySearch(numberList, numberToFind, low, mid - 1)


if __name__ == "__main__":
    numberList = [
        1,
        2,
        5,
        7,
        9,
        15,
        20,
        21,
        22,
        89,
        100
    ]

    numberToFind = int(raw_input("Which number do you want me to find: "))

    if (binarySearch(numberList, numberToFind, 0, len(numberList) - 1)):
        print("The number " + str(numberToFind) + " is in the list")
    else:
        print("The number " + str(numberToFind) + " is not in the list")