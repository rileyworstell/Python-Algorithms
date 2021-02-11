"""
Implement depth first search method on node class.
"""


# O(v + e) Time & O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for i in self.children:
            i.depthFirstSearch(array)
        return array


A = Node('A')
A.addChild('B').addChild('C').addChild('D')
A.addChild('E').addChild('F')

print(A.depthFirstSearch([]))
