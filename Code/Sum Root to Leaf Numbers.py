# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], number: int) -> int:                       #Traverse tree with the number from root to the parent of current node.
        if not root:                                                                        #If current node is none, return 0.
            return 0
        number = number * 10 + root.val                                                     #Update number to include current node.
        if not root.left and not root.right:                                                #If current node is leaf, return number.
            return number
        return self.traverse(root.left, number) + self.traverse(root.right, number)         #Return the sum of result of traversing left child and right child.
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)                                                       #Start traversing from root with 0.
