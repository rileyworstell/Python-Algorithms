"""
Implement breadth first search method on node class.
"""


# O(v + e) Time & O(v) space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            first = queue.pop(0)
            array.append(first)
            for child in first.children:
                queue.append(child)
        return array


A = Node('A')
A.addChild('B').addChild('C').addChild('D')
A.addChild('E').addChild('F')

print(A.breadthFirstSearch([]))
