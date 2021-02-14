"""
Return all permutations of an array.
"""


# O(n^2 * n!) Time & O(n *n!) Space
def get_permutations(array):
    permutations = []
    helper(array, [], permutations)
    return permutations


def helper(array, perm, perms):
    if len(array) == 0 and len(perm):
        perms.append(perm)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i+1:]
            new_perm = perm + [array[i]]
            helper(new_array, new_perm, perms)


array = [1, 2, 3]
print(get_permutations(array))
