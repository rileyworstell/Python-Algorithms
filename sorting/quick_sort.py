"""
Write a function that takes in an array of integers and returns a sorted version. 
Use quick sort.
"""


# O(nlog(n)) Time & O(log(n)) Space on Average
def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, start_pointer, end_pointer):
    if start_pointer >= end_pointer:
        return
    pivot = start_pointer
    l_pointer = start_pointer + 1
    r_pointer = end_pointer
    while r_pointer >= l_pointer:
        if array[l_pointer] > array[pivot] and array[r_pointer] < array[pivot]:
            array[l_pointer], array[r_pointer] = array[r_pointer], array[l_pointer]
        if array[l_pointer] <= array[pivot]:
            l_pointer += 1
        if array[r_pointer] >= array[pivot]:
            r_pointer -= 1
    array[pivot], array[r_pointer] = array[r_pointer], array[pivot]
    if r_pointer - 1 - start_pointer < end_pointer - (r_pointer+1):
        quick_sort_helper(array, start_pointer, r_pointer-1)
        quick_sort_helper(array, r_pointer+1, end_pointer)
    else:
        quick_sort_helper(array, r_pointer + 1, end_pointer)
        quick_sort_helper(array, start_pointer, r_pointer - 1)


array = [8, 5, 2, 9, 5, 6, 3]

print(quick_sort(array))
