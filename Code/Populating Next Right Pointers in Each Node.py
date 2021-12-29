"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:                   #If reach the bottom, return.
            return root
        root.left.next = root.right                     #Next pointer of left child of current node points to right child of current node.
        if root.next:                                   #Because it's a perfect binary tree, if current node isn't the rightmost node of current level,
            root.right.next = root.next.left            #Current node must have right child and next node must have left child and the former node's next node is the latter node.
        root.left = self.connect(root.left)             #Recursively connect left subtree.
        root.right = self.connect(root.right)           #Recursively connect right subtree.
        return root
