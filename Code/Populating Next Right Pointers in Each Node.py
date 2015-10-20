# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root==None or root.left==None:              #If reach the bottom, return.
            return
        root.left.next=root.right                      #Next pointer of left child of current node points to right child of current node.
        if root.next!=None:                            #Because it's a perfect binary tree, if current node isn't the rightmost node of current level,
            root.right.next=root.next.left             #current node must have right child and next node must have left child and the former node's next node is the latter node.
        self.connect(root.left)                        #recursion
        self.connect(root.right)
