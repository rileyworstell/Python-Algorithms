"""
Given a 2D array of distinct integegers where each row and column is sorted, find the target value.
"""


# O(n + m) Time & O(1) Space
def searchInSortedMatrix(matrix, target):
    diagonal = 0
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    minimum_diagonal = min(r, c)
    position = [0, 0]
    while diagonal < minimum_diagonal:
        if matrix[diagonal][diagonal] == target:
            return [diagonal, diagonal]
        elif matrix[diagonal][diagonal] < target:
            if diagonal < minimum_diagonal:
                diagonal += 1
        elif matrix[diagonal][diagonal] > target:
            for i in range(0, diagonal):
                if matrix[i][diagonal] == target:
                    return [i, diagonal]
                if matrix[diagonal][i] == target:
                    return [diagonal, i]
            diagonal += 1  # look at

    if matrix[diagonal][diagonal] == target:
        return [diagonal, diagonal]
    for i in range(0, diagonal):
        if matrix[i][diagonal] == target:
            return [i, diagonal]
        if matrix[diagonal][i] == target:
            return [diagonal, i]
    position = [diagonal, diagonal]
    if r < c:
        while position[1] <= c:
            # go up column
            for i in range(0, position[1]):
                if matrix[i][position[1]] == target:
                    return [i, position[1]]
            position[1] += 1
    else:
        while position[0] <= r:
            for i in range(0, position[0]):
                if matrix[position[0]][i] == target:
                    return [position[0], i]
            position[0] += 1
    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
target = 99
print(searchInSortedMatrix(matrix, target))
