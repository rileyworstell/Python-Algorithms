"""
Write a function that takes in two non empty arrays of integers, finds the pair of numbers
(one from each array whose closes difference is zero, returning an array containing these two n
umbers with the number from the first array in the first position.)
"""


# O(nlog(n) + mlog(m)) Time & O(1) Space
def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    one_pointer = 0
    two_pointer = 0
    difference = None
    answer = [array_one[0], array_two[0]]
    while ((one_pointer < len(array_one)) and (two_pointer < len(array_two))):
        if (abs(array_two[two_pointer] - array_one[one_pointer]) == 0):
            return [array_one[one_pointer], array_two[two_pointer]]
        if (abs(array_two[two_pointer] - array_one[one_pointer]) < abs(answer[0] - answer[1])):
            answer = [array_one[one_pointer], array_two[two_pointer]]
        if (array_two[two_pointer] > array_one[one_pointer]):
            one_pointer += 1
        else:
            two_pointer += 1
    return answer


array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]
print(smallest_difference(array_one, array_two))  # [28, 26]
