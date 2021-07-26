# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:                                                                                                    #If nums is empty, return none.
            return None
        mid = len(nums) // 2                                                                                            #Find the index of element in the middle in nums.
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))            #Create TreeNode with nums[mid] as value and left child and right child created recursively.
