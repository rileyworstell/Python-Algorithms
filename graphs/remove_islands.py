"""
Remove islands from a matrix.
An island is a group of ones that are not touching the border of the matrix anywhere.
"""


# O(n*m) Time & O(n*m) Space
def removeIslands(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if isIsland([i, j], matrix) == True:
                matrix = replaceIsland([i, j], matrix)
    return matrix


def replaceIsland(starting_point, matrix):
    x = len(matrix[0]) - 1
    y = len(matrix) - 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    isAnIsland = None
    queue = []
    visited = [[0 for y in matrix[0]] for x in matrix]
    queue.append(starting_point)
    while queue:
        current_point = queue.pop(0)
        matrix[current_point[0]][current_point[1]] = 0
        visited[current_point[0]][current_point[1]] = 1
        for i in range(len(dx)):
            # if the new y is in the bounds of the matrix
            if current_point[0] + dy[i] >= 0 and current_point[0] + dy[i] <= y:
                # if the new x is in the bounds of thye matrix
                if current_point[1] + dx[i] >= 0 and current_point[1] + dx[i] <= x:
                    # if the value is a 1 meaning is it land
                    if matrix[current_point[0] + dy[i]][current_point[1] + dx[i]] == 1:
                        # if we have not already visited it then add it to the queue
                        if visited[current_point[0] + dy[i]][current_point[1] + dx[i]] != 1:
                            queue.append(
                                [current_point[0] + dy[i], current_point[1] + dx[i]])
    return matrix


def isIsland(starting_point, matrix):
    x = len(matrix[0]) - 1
    y = len(matrix) - 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    isAnIsland = None
    queue = []
    visited = [[0 for y in matrix[0]] for x in matrix]
    queue.append(starting_point)
    while queue:
        current_point = queue.pop(0)
        if (current_point[0] == 0 or current_point[0] == y) or (current_point[1] == 0 or current_point[1] == x):
            return False
        visited[current_point[0]][current_point[1]] = 1
        for i in range(len(dx)):
            # if the new y is in the bounds of the matrix
            if current_point[0] + dy[i] >= 0 and current_point[0] + dy[i] <= y:
                # if the new x is in the bounds of thye matrix
                if current_point[1] + dx[i] >= 0 and current_point[1] + dx[i] <= x:
                    # if the value is a 1 meaning is it land
                    if matrix[current_point[0] + dy[i]][current_point[1] + dx[i]] == 1:
                        # if we have not already visited it then add it to the queue
                        if visited[current_point[0] + dy[i]][current_point[1] + dx[i]] != 1:
                            queue.append(
                                [current_point[0] + dy[i], current_point[1] + dx[i]])
                            # visited[current_point[0] + dy[i]
                            #         ][current_point[1] + dx[i]] = 1
    return True


# matrix = [
#     [1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 1, 1],
#     [0, 0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1, 0],
#     [1, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 0, 1]
# ]
matrix = [
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0]
]

# print(remove_islands(matrix))
# print(isIsland([1, 6], matrix))
# print(replaceIsland([1, 6], matrix))
# print(replaceIsland([4, 2], matrix))
x = removeIslands(matrix)
# for i in x:
#     print(i)
