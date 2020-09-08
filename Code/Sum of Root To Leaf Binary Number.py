# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode, path: int, numbers: List[int]) -> None:      #Traverse the tree.
        if root is None:
            return
        path = path << 1 | root.val                                                 #Update the sum in path.
        if root.left is None and root.right is None:                                #If current node is leaf, add sum to numbers list.
            numbers.append(path)
        else:                                                                       #Otherwise keep traversing through left subtree and right subtree.
            self.traverse(root.left, path, numbers)
            self.traverse(root.right, path, numbers)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        numbers = []
        self.traverse(root, 0, numbers)
        return sum(numbers)                                                         #Return the sum of numbers list.
