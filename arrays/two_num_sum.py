"""
Write a function that takes in a non-empty array of distinct integers and an integer
representing a target sum. If any two numbers in the input array sum up to the target sum, the
function should return them in an array, in any order. If not two numbers sum up to the target sum,
the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer
to itself in order to obtain the target sum.
You can assume there will be at most one pair of numbers summing up to the target sum.
"""

# O(n) time | O(n) space
# def two_number_sum(array, targetSum):
#     arr = []
#     for i in array:
#         if (targetSum - i) in arr:
#             x = arr.index(targetSum-i)
#             return [targetSum-i, i]
#         arr.append(i)
#     return []


# O(nlog(n)) time | O(1) space
def two_number_sum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(two_number_sum(array, targetSum))
