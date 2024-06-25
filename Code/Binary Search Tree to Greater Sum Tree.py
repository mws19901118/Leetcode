# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(root: TreeNode, greaterSum: int) -> int:        #Traverse tree with sum of keys greater than root then update each node and return the sum of tree.
            if not root:                                             #If root is none, return 0.
                return 0
            rightSum = traverse(root.right, greaterSum)              #Traverse right subtree and get right subtree sum.
            totalSum = rightSum + root.val                           #Calculate total sum of root and right subtree.
            root.val += greaterSum + rightSum                        #Update root.val.
            return totalSum + traverse(root.left, root.val)          #Traverse left subtree and add left subtree sum to total sum then return.

        traverse(root, 0)                                            #Traverse from root with 0 greater sum.
        return root                                                  #Return root after traverse.
