"""
Given a string of available characters and a string representing a document that you need to generate.
Write a function that determines if you can generate the document using the available characters. If you can 
you should return true, if not then false.
"""


def generateDocument(characters, document):
    myHash = {}
    for i in range(len(characters)):
        if characters[i] not in myHash:
            myHash[characters[i]] = 1
        else:
            myHash[characters[i]] += 1
    for j in document:
        if j not in myHash:
            return False
        if myHash[j] > 0:
            myHash[j] -= 1
        elif myHash[j] == 0:
            return False
    return True


characters = "Bste!hetsi ogEAxpelrt X "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))
