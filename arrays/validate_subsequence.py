"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of th efirst one.
A subseq of an array is a set of numbers that aren't necessarily adjacenti int the array but that are in the same order as they appear
in the array. For instance, the numbers [1, 3, 4] form a subsdq of the array [1, 2, 3, 4] and so do numbers [2, 4].
"""


# O(n) Time & O(1) Space
def is_valid_subsequence(array, sequence):
    pointerArray = 0
    pointerSequence = 0
    while pointerSequence < len(sequence):
        if pointerSequence == len(sequence)+1:
            return True
        if pointerArray == len(array):
            return False
        if sequence[pointerSequence] != array[pointerArray]:
            pointerArray += 1
        else:
            pointerArray += 1
            pointerSequence += 1
    return True


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_valid_subsequence(array, sequence))
