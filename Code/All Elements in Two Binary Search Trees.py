# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: TreeNode, s: List[int]):                                 #BST inorder traversal.
        if not root:
            return
        self.traverse(root.left, s)
        s.append(root.val)
        self.traverse(root.right, s)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        s1, s2 = [], []
        self.traverse(root1, s1)                                                      #Traverse tree1.
        self.traverse(root2, s2)                                                      #Traverse tree2.
        result = []
        i, j = 0, 0
        while i < len(s1) and j < len(s2):                                            #Merge result.
            if s1[i] <= s2[j]:
                result.append(s1[i])
                i += 1
            else:
                result.append(s2[j])
                j += 1
        if i < len(s1):
            result.extend(s1[i:])
        else:
            result.extend(s2[j:])
        return result
