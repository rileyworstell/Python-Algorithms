"""

"""


def get_permutations(array):
    permutations = []
    for i in range(len(array)):
        x = perm_helper(array[:i] + array[i+1:])
        for j in x:
            permutations.append([array[i], j[0], j[1]])
    return permutations


def perm_helper(array):
    if len(array) == 2:
        return [[array[0], array[1]], [array[1], array[0]]]


array = [1, 2, 3, 4]
print(get_permutations(array))
