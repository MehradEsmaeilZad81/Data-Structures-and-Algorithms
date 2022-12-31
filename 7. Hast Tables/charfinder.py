def findFirstNonRepeatedChar(str):
    charDict = {}
    for char in str:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    for char in str:
        if charDict[char] == 1:
            return char
    return None


# Test
str = "a green apple"
print(findFirstNonRepeatedChar(str))
