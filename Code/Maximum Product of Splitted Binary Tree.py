# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getSum(self, root: Optional[TreeNode], nodeSum: List[int]):
        if root is None:                                                                                  #If not is None, return 0.
            return 0
        nodeSum.append(root.val + self.getSum(root.left, nodeSum) + self.getSum(root.right, nodeSum))     #Calculate subtree sum of current node and append it to nodeSum.
        return nodeSum[-1]                                                                                #Return subtree sum of current node.
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        nodeSum = []                                                                                      #Store the subtree sum of each node.
        totalSum = self.getSum(root, nodeSum)                                                             #Calculate total sum and subtree sum of each node.
        return max(x * (totalSum - x) for x in nodeSum) % (10 ** 9 + 7)                                   #The max product is max(x * (totalSum - x)), x is each subtree sum. Return the remain after modulo operation.
