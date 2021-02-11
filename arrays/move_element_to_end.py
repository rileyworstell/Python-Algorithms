"""
You're given an array of integers and an integer. Write a function that moves all instances of that integer
in the array to the end of the array and returns the array.
Should perform in place.
"""


# O(n) Time & O(1) Space
def move_element_to_end(array, to_move):
    end_pointer = len(array) - 1
    beginning_pointer = 0

    while (beginning_pointer < end_pointer):
        while (array[end_pointer] == to_move) and (end_pointer > 0):
            end_pointer -= 1
        if (array[beginning_pointer] == to_move) and (beginning_pointer < end_pointer):
            array[beginning_pointer], array[end_pointer] = array[end_pointer], array[beginning_pointer]
        beginning_pointer += 1
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2
print(move_element_to_end(array, to_move))
