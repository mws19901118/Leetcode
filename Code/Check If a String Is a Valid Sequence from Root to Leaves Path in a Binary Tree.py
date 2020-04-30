# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root is None or len(arr) == 0 or root.val != arr[0]:                                         #If root is none, arr is empty or root value does not equal to the first number in arr, return false.
            return False
        if root.left is None and root.right is None:                                                    #If root is leaf node, check if arr has reached its end.
            return len(arr) == 1
        return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])    #DFS through left child and right child respectively.
