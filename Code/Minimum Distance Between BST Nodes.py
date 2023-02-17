# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def traverse(root: Optional[TreeNode]) -> (int, int, int):                                                  #Traverse subtree and return the min distance between nodes in subtree and min value of subtree and max value of subtree.
            if not root.left and not root.right:
                return 100001, root.val, root.val
            elif root.left and not root.right:
                left = traverse(root.left)
                return min(left[0], root.val - left[2]), left[1], root.val
            elif not root.left and root.right:
                right = traverse(root.right)
                return min(right[0], right[1] - root.val), root.val, right[2]
            else:
                left, right = traverse(root.left), traverse(root.right)
                return min(left[0], right[0], root.val - left[2], right[1] - root.val), left[1], right[2]
        return traverse(root)[0]                                                                                    #Return the min distance from root.
