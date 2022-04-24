# https://leetcode.com/problems/find-duplicate-subtrees/
# Definition for a binary tree node.
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root):
        hashMap = {}
        ans = []
        self.helper(root, hashMap, ans)
        return ans


    def helper(self, tree, hashMap, ans):
        if tree is not None:
            left = self.helper(tree.left, hashMap, ans)
            right = self.helper(tree.right, hashMap, ans)
            build = (tree.val, (left), (right))
            if build in hashMap:
                if hashMap[build] != False:
                    ans.append(tree)
                hashMap[build] = False
            else:
                hashMap[build] = True
            return build
        return ()
        



tree = Tree(1)
tree.right = Tree(3)
tree.right.right = Tree(4)
tree.right.left = Tree(2)
tree.right.left.left = Tree(4)
tree.left = Tree(2)
tree.left.left = Tree(4)
x = Solution()
print(x.findDuplicateSubtrees(tree)) # [[2, 4], [4]]
