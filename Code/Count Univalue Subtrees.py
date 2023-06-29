# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, bool, int):                                                                            #Traverse tree, return the total univalue subtree count under root, if current substree is univalue and root value(could be none) as a tuple.
            if not root:                                                                                                                       #If root is none, return (0, True, None) as we treat it as univalue but don't count it.
                return 0, True, None
            leftCount, leftIsUnivalue, leftValue = traverse(root.left)                                                                         #Traverse left child.
            rightCount, rightIsUnivalue, rightValue = traverse(root.right)                                                                     #Traverse right child.
            rootIsUnivalue = leftIsUnivalue and rightIsUnivalue and leftValue in [None, root.val] and rightValue in [None, root.val]           #Current substree is univalue if both left subtree and right subtree is univalue and their value is eother none or same as value of root.
            return leftCount + rightCount + int(rootIsUnivalue), rootIsUnivalue, root.val                                                      #Return the sum of univalue subtree and if current substree is univalue and root value. 
        
        return traverse(root)[0]                                                                                                               #Return the total univalue subtree count from the result of traverse(root).
