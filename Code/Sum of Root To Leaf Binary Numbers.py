# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode], b: int) -> int:                        #Traverse the tree to get the sum of root to leaf.
            if not node:                                                              #If node is none, return 0.
                return 0
            b = (b << 1) | node.val                                                   #Update the binary number from root to current node.
            if not node.left and not node.right:                                      #If current node is leaf, return the binary number.
                return b
            return traverse(node.left, b) + traverse(node.right, b)                   #Otherwise keep traversing through left subtree and right subtree.
        return traverse(root, 0)                                                      #Return the result of traversing from root.
