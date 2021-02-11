"""
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in zigzag.
zigzag order starts at top left goes down and proceeds in a zigzag pattern all the way to the bottom right corner.
"""


# O(n) Time & O(n) Space
def zig_zag_traverse(array):
    position = [0, 0]
    answer = []
    answer.append(array[position[0]][position[1]])
    position[0] += 1
    direction = 'up'
    if len(array) == 1:
        return array[0]
    while position != [len(array)-1, len(array[len(array)-1]) - 1]:
        while ((0 <= position[0] < len(array)) and (0 <= position[1] < len(array[0]))):
            answer.append(array[position[0]][position[1]])
            if direction == 'up':
                position[0] -= 1
                position[1] += 1
            elif direction == 'down':
                position[0] += 1
                position[1] -= 1
        if direction == 'up':
            position[0] += 1
            position[1] -= 1
            if ((position[0] == 0) and (position[1] != len(array[0])-1)):
                position[1] += 1
            else:
                position[0] += 1
            direction = 'down'
        elif direction == 'down':
            position[0] -= 1
            position[1] += 1
            if (position[1] == 0) and (position[0] < len(array) - 1):
                position[0] += 1
            else:
                position[1] += 1
            direction = 'up'
    answer.append(array[len(array)-1][len(array[len(array)-1]) - 1])
    return answer


array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
]

# array = [
#     [1, 3, 4, 10, 11],
#     [2, 5, 9, 12, 19],
#     [6, 8, 13, 18, 20],
#     [7, 14, 17, 21, 24],
#     [15, 16, 22, 23, 25]
# ]
# array = [[1]]
# array = [[1, 3, 4, 7, 8], [2, 5, 6, 9, 10]]
print(zig_zag_traverse(array))
