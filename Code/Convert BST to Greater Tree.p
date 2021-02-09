# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode, traversedSum: int) -> int:     #Traverse tree in post order, update node and return the sum of tree. TraversedSum is the sum of values of nodes have been traversed; those nodes are all greater than root.
        if root is None:                                              #Return 0 if root is none.
            return 0
        currentRootValue = root.val                                   #Record current root value.
        rightSum = self.traverse(root.right, traversedSum)            #Traverse right subtree and get its sum.
        root.val += traversedSum + rightSum                           #Add traversedSum and rightSum to root value.
        leftSum = self.traverse(root.left, root.val)                  #Traverse left subtree and get its sum.
        return currentRootValue + leftSum + rightSum                  #Return the sum of tree.
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.traverse(root, 0)                                        #Traverse root with traversed sum starting from 0.
        return root
