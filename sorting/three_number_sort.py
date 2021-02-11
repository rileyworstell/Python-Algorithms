"""
Given array of integers and another array of 3 distinct integers.
first array only contains integers in the second array.
second array represents the desired order for the integers of the first array.
"""


def three_number_sort(array, order):
    beginning_pointer = 0
    end_pointer = len(array)-1
    for i in range(len(array)):
        if array[i] == order[0]:
            array[beginning_pointer], array[i] = array[i], array[beginning_pointer]
            beginning_pointer += 1
    for j in range(len(array)-1):
        if array[j] == order[2]:
            array[end_pointer], array[j] = array[j], array[end_pointer]
            end_pointer -= 1
    return array


array = [0, 10, 10, 10, 10, 10, 25, 25, 25, 25, 25]
order = [25, 10, 0]
print(three_number_sort(array, order))
