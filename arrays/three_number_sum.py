"""
Write a function that takes in a non empty array of distinct integers and an integer representing a target sum.
The function finds all should find all triplets in the array that sum up to the target sum and return a 2d array of these triplets
"""


# O(n^2) Time & O(n) Space
def three_number_sum(array, target_sum):
    ansArr = []
    anAns = []
    ansDict = {}
    array.sort()
    for i in range(len(array)):
        lP = 0
        rP = len(array) - 1
        while lP < rP:
            if lP == i:
                lP += 1
            elif rP == i:
                rP -= 1
            elif ((array[lP] + array[rP] + array[i]) == target_sum):
                anAns = [array[lP], array[rP], array[i]]
                anAns.sort()
                if (str(anAns[0]) + ',' + str(anAns[1]) + ',' + str(anAns[2])) not in ansDict:
                    ansDict[str(anAns[0]) + ',' + str(anAns[1]) + ',' +
                            str(anAns[2])] = True
                    ansArr.append(anAns)
                lP += 1
                rP -= 1
            elif array[lP] + array[i] + array[rP] > target_sum:
                rP -= 1
            elif array[lP] + array[i] + array[rP] < target_sum:
                lP += 1

    return ansArr


array = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0
print(three_number_sum(array, target_sum))
