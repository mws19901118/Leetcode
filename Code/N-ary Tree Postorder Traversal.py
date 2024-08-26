"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(root: 'Node') -> None:        #Post order traversal.
            if not root:
                return
            for x in root.children:
                traverse(x)
            result.append(root.val)
        result = []
        traverse(root)
        return result
