# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache                                                                                 #Cache result.
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n & 1:                                                                      #If n is even, it cannot form a valid FBT, so return empty list directly.
            return []
        if n == 1:                                                                         #If n is 1, return a list with a one-node binary tree.
            return [TreeNode(0)]
        result = []
        for i in range(1, n - 1, 2):                                                       #Enumerate all possible count of nodes in left subtree, which should also be a FBT.
            left, right = self.allPossibleFBT(i), self.allPossibleFBT(n - i - 1)           #Get the possible FBT of left subtree and possible FBT of right subtree.
            for x, y in product(left, right):                                              #Traverse the combination of each FBT pair in left and right.
                result.append(TreeNode(0, x, y))                                           #Append a FBT with x as left child of root and y as right child of root.
        return result                                                                      #Return result.
