# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode], number: int) -> int:                   #Traverse tree with the number from root to the parent of current node.
            if not root:                                                              #If current node is none, return 0.
                return 0
            number = number * 10 + root.val                                           #Update number to include current node.
            if not root.left and not root.right:                                      #If current node is leaf, return number.
                return number
            return traverse(root.left, number) + traverse(root.right, number)         #Return the sum of result of traversing left child and right child.
        return traverse(root, 0)                                                      #Return thr result of traversing from root with 0.
