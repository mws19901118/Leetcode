# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToSet(self, root: Optional[TreeNode], s: set) -> None:                   #Put all numbers in a BST into a set.
        if not root:
            return
        s.add(root.val)
        self.bstToSet(root.left, s)
        self.bstToSet(root.right, s)
        
    def search(self, root: Optional[TreeNode], s: set, k: int) -> bool:             #Search for 2 sum pair.
        if not root:                                                                #If root is none, return false.
            return False
        if root.val * 2 != k and k - root.val in s:                                 #If root.val * 2 != k and k - root.val in s, we found a 2 sum pair, return true.
            return True
        return self.search(root.left, s, k) or self.search(root.right, s, k)        #Keep searching in left subtree and right subtree.
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        self.bstToSet(root, s)
        return self.search(root, s, k)
