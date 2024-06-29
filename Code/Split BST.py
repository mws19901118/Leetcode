# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:                                                                  #If root is none, return none and none.
            return [None, None]
        if root.val > target:                                                         #If root.val is greater than target, target is in left subtree, if exist.
            leftNotGreater, leftGreater = self.splitBST(root.left, target)            #Split left subtree.
            root.left = leftGreater                                                   #Replace root.left with leftGreater.
            return [leftNotGreater, root]                                             #Return leftNotGreater and root.
        else:                                                                         #Otherwise, target is in right subtree, if exist.
            rightNotGreater, rightGreater = self.splitBST(root.right, target)         #Split right subtree.
            root.right = rightNotGreater                                              #Replace root.right with rightNoeGreater.
            return [root, rightGreater]                                               #Return root and rightGreater.
