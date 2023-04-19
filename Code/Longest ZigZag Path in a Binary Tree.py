# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode], length: int, directionIsLeft: bool) -> int:                                                                                                    #Traverse with the length and direction of zigzag path from parent.
            if not root:                                                                                                                                                                      #If root is none, return 0.
                return 0
            return max(length, traverse(root.left, (length + 1) if not directionIsLeft else 1, True), traverse(root.right, (length + 1) if directionIsLeft else 1, False))                    #Return the max of length from parent and result of traversing left child and right child.
        
        return max(traverse(root.left, 1, True), traverse(root.right, 1, False))                                                                                                              #Return the max of traversing the left child and right child of root.
