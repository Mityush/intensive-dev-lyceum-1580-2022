def invert(dictionary):
    newDictionary = {}
    for index in dictionary:
        newDictionary[dictionary[index]] = index
    return newDictionary
