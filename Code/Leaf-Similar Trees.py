# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(root: Optional[TreeNode]) -> None:              #Traverse tree to get all leaves.
            if not root:                                            #If root is none, return.
                return
            if not root.left and not root.right:                    #If root is leaf, return its value in generator.
                yield root.val
            yield from getLeaf(root.left)                           #Return the leaves in left subtree in generator.
            yield from getLeaf(root.right)                          #Return the leaves in right subtree in generator.
        return list(getLeaf(root1)) == list(getLeaf(root2))         #Judging if the leaf sequence in 2 trees are same.
