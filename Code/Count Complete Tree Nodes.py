# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lh, rh = 0, 0                                                                       #Record the height of left tree and height of right tree.
        l, r = root, root
        while l.left is not None:                                                           #Because it's complete tree, the length of the left most branch is the height of left tree.
            l = l.left
            lh += 1
        while r.right is not None:                                                          #Because it's complete treem the length of the right most branch is the height of right tree.
            r = r.right
            rh += 1
        if lh == rh:                                                                        #If left height equals right height, it's a perfect tree and return 2 ^ (lh + 1) - 1.
            return pow(2, lh + 1) - 1
        else:                                                                               #If it's not a perfect tree, calculate number of nodes recursibely.
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
