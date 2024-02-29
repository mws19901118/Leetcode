# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int):                                                                #Traverse each node and return the count of nodes equal to sum of descendants in its subtree also the sum of its subtree.
            if not root:                                                                                                     #If root is none, return 0 and 0.
                return 0, 0
            leftResult, leftSum = traverse(root.left)                                                                        #Traverse root.left.
            rightResult, rightSum = traverse(root.right)                                                                     #Traverse root.right.
            return leftResult + rightResult + int(root.val == leftSum + rightSum), leftSum + rightSum + root.val             #Return result for current root, checking if value of root equals the sum of leftSum and rightSum; also calculate the whole sum.
        
        return traverse(root)[0]                                                                                             #Return the first result of traversing from root.
