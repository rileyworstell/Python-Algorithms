"""
Find Kth largest value in the BST. Duplicate values are not considered.
"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(d + k) Time & O(d) Space
def findKthLargestValueInBst(tree, k, arr=[], answer=None):
    if tree is not None:
        if answer == None:
            answer = findKthLargestValueInBst(tree.right, k, arr, answer)
            arr.append(tree.value)
            if len(arr) == k:
                answer = arr[len(arr)-1]
            answer = findKthLargestValueInBst(tree.left, k, arr, answer)
    return answer


# Create Tree
tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.right = BST(5)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.left.right = BST(14)
tree.right.right = BST(22)
"""
Tree
            10
        5        15
      2   5    13   22
    1            14
"""

print(findKthLargestValueInBst(tree, 3))
