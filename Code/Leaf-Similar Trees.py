# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], leaves: List[int]) -> None:                        #Store leaf values in sequence in an array by pre-order traversal recursively.
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        self.traverse(root.left, leaves)
        self.traverse(root.right, leaves)                                                           

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        self.traverse(root1, leaves1)                                                               #Find the leaf values of root1.
        self.traverse(root2, leaves2)                                                               #Find the leaf values of root2.
        return leaves1 == leaves2                                                                   #Compare.
