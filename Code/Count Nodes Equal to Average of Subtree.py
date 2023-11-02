# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(node: Optional[TreeNode]) -> (int, int, int):                    #Traverse tree to find numbers of nodes equal to average, count of nudes and sum of nodes in subtree.
            if not node:                                                              #If node is none, return 0, 0, 0
                return 0, 0, 0
            count, sum = 1, node.val                                                  #Initially, count is 1 and sum is node.val.
            leftResult, leftCount, leftSum = traverse(node.left)                      #Get the result from left subtree.
            rightResult, rightCount, rightSum = traverse(node.right)                  #Get the result from right subtree.
            count += leftCount + rightCount                                           #Update count.
            sum += leftSum + rightSum                                                 #Update sum.
            result = leftResult + rightResult + int(sum // count == node.val)         #Current result is the sum of leftResult and rightResult and if current node is same as average.
            return result, count, sum                                                 #Return (result, count, sum)
        
        return traverse(root)[0]                                                      #Return the first result of traverse from root.
