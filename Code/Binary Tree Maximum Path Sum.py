# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root: Optional[TreeNode]) -> (int, int):
        if not root:                                                                                                                                                                                                #If root is none, return 0 and 0.
            return (0, 0)
        l, r = self.traverse(root.left), self.traverse(root.right)                                                                                                                                                  #Get the result from left child and right child.
        maxPathSumFromRoot = max(root.val, root.val + l[1], root.val + r[1])                                                                                                                                        #Find the max path sum from root.
        maxPathSum = max(l[0] if root.left else maxPathSumFromRoot, r[0] if root.right else maxPathSumFromRoot, (root.val + l[1] + r[1]) if root.left and root.right else maxPathSumFromRoot, maxPathSumFromRoot)   #Max path sum is the max of max path sum from root, max path sum of left child if left child is not none, max path sum of right child if right child is not none and root.val plus both max path sum of both children if both children is not none.
        return maxPathSum, maxPathSumFromRoot                                                                                                                                                                       #Return maxPathSum and maxPathSumFromRoot.
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)[0]
