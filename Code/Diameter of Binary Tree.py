# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int):                                                #For each node, find the height of node plus one and the diameter of the subtree.
            if not root:
                return 0, 0
            leftHeight, leftMax = traverse(root.left)                                                        #Traverse through left subtree.
            rightHeight, rightMax = traverse(root.right)                                                     #Traverse through right subtree.
            return max(leftHeight, rightHeight) + 1, max(leftMax, rightMax, leftHeight + rightHeight + 1)    #Calculete the height and diameter. Diameter should be the max of left subtree diameter, right subtree diameter and the sum of left child height plus one and right child hight plus one.
        return traverse(root)[1] - 1                                                                         #Return the diameter.
