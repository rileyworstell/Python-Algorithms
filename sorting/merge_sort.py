"""
sort using merge sort
"""


# O(nlog(n)) Time & O(nlog(n)) Space
def merg_sort(array):
    new_arr = []
    divider = len(array) // 2
    part_1 = array[:divider]
    part_2 = array[divider:]
    if len(part_1) > 1 or len(part_2) > 1:
        part_1 = mergeSort(part_1)
        part_2 = mergeSort(part_2)
    pointer_1 = 0
    pointer_2 = 0
    while (pointer_1 < len(part_1)) or (pointer_2 < len(part_2)):
        if pointer_2 == len(part_2):
            new_arr.append(part_1[pointer_1])
            pointer_1 += 1
        elif pointer_1 == len(part_1):
            new_arr.append(part_2[pointer_2])
            pointer_2 += 1
        elif part_1[pointer_1] < part_2[pointer_2]:
            new_arr.append(part_1[pointer_1])
            pointer_1 += 1
        elif part_1[pointer_1] >= part_2[pointer_2]:
            new_arr.append(part_2[pointer_2])
            pointer_2 += 1
    return new_arr


# array = [8, 5, 2, 9, 5, 6, 3]
array = [3, 2, 1, 0]
# array = [1, 3, 2]
print(merge_sort(array))
