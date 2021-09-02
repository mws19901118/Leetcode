# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtracking(self, nums: List[int]) -> List[Optional[TreeNode]]:    #Generate a list of unique BST for nums array.
        if not nums:                                                        #If nums is empty, return [None].
            return [None]
        result = []                                                         #Initialize result.
        for i, x in enumerate(nums):                                        #Traverse nums.
            left = self.backtracking(nums[:i])                              #Generate all possible left subtrees for root x.
            right = self.backtracking(nums[i + 1:])                         #Generate all possible right subtrees for root x.
            for l, r in product(left, right):                               #Append BST with root x and each left subtree and each right subtree to result. 
                result.append(TreeNode(x, l, r))
        return result                                                       #Return result.
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.backtracking([i for i in range(1, n + 1)])              #Generate unique BST for [1, 2, ..., n].
