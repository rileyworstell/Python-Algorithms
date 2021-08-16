
# return which number is unique
# time = O(n) space = O(1)
def whichUnique(arr):
    totalSum = sum(arr)
    uniqueSum = sum(set(arr))
    return (2 * uniqueSum) - totalSum


print(whichUnique([2, 2, 1, 1, 4]))
# 4
