# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flattenAndReturnTail(self, root: TreeNode) -> TreeNode:
        if not root:                                                        #If root is none, return none.
            return None
        if not root.left and not root.right:                                #If root is leaf node, return root.
            return root
        rightTail = self.flattenAndReturnTail(root.right)                   #Flattern right subtree and get tail.
        leftTail = self.flattenAndReturnTail(root.left)                     #Flattern left subtree and get tail.
        if leftTail:                                                        #If root has left child, point right of left tail to right subtree of root, then move right left child to right child.
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        return rightTail if rightTail else leftTail                         #Id right tail is not none, return right tail; otherwise, return left tail.
            
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenAndReturnTail(root)                                     #Flattern.
