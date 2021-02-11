"""
Write a function that takes in an n x m matrix and returns a 1d array of all the arrays elements in spiral order.
Sprial starts at top left, goes right, then down.
"""


# O(N) Time & O(N) Space where N is total number of values in array
def spiral_traverse(array):
    directions = ['right', 'down', 'left', 'up']
    direction_pointer = 0
    answer = []
    pointer = [-1, -1]
    while True:
        if directions[direction_pointer] == 'right':
            pointer[0] += 1
            pointer[1] += 1
            if (array[pointer[0]][pointer[1]] == None):
                return answer
            while (pointer[1] < len(array[pointer[0]])) and (array[pointer[0]][pointer[1]] != None):
                answer.append(array[pointer[0]][pointer[1]])
                array[pointer[0]][pointer[1]] = None
                pointer[1] += 1
            direction_pointer += 1
        elif directions[direction_pointer] == 'down':
            pointer[1] -= 1
            pointer[0] += 1
            if (pointer[0] >= len(array)):
                return answer
            if (array[pointer[0]][pointer[1]] == None):
                return answer
            while (pointer[0] < len(array)) and (array[pointer[0]][pointer[1]] != None):
                answer.append(array[pointer[0]][pointer[1]])
                array[pointer[0]][pointer[1]] = None
                pointer[0] += 1
            direction_pointer += 1
        elif directions[direction_pointer] == 'left':
            pointer[0] -= 1
            pointer[1] -= 1
            if ((array[pointer[0]][pointer[1]] == None)):
                return answer
            while (pointer[1] >= 0) and (array[pointer[0]][pointer[1]] != None):
                answer.append(array[pointer[0]][pointer[1]])
                array[pointer[0]][pointer[1]] = None
                pointer[1] -= 1
            direction_pointer += 1
        elif directions[direction_pointer] == 'up':
            pointer[0] -= 1
            pointer[1] += 1
            if (array[pointer[0]][pointer[1]] == None):
                return answer
            while (pointer[0] >= 0) and (array[pointer[0]][pointer[1]] != None):
                answer.append(array[pointer[0]][pointer[1]])
                array[pointer[0]][pointer[1]] = None
                pointer[0] -= 1
            direction_pointer = 0


# array = [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7],
# ]
array = [[1, 3, 4, 5]]
print(spiral_traverse(array))
