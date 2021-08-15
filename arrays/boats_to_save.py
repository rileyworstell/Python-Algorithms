# 2 people max per boat, return number of boats it will take to
# return the people denoted by an array with their weights and the limit being the maximum weight a boat can carry.

# O(nlog(n)) time (because we sort the array) O(n) space
def boats_to_save(people, limit):
    boatsNum = 0
    people.sort()
    lPointer = 0
    rPointer = len(people) - 1
    while lPointer <= rPointer:
        if people[lPointer] + people[rPointer] > limit:
            boatsNum += 1
            rPointer -= 1
        else:
            boatsNum += 1
            rPointer -= 1
            lPointer += 1
    return boatsNum


    # 4 [[1, 3], [1, 3], [2, 2], [4]]
print(boats_to_save([1, 3, 2, 2, 1, 3, 4], 4))
