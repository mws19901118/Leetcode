# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):                                      #Morris Preorder Traversal, similar to Recover Binary Search Tree.
        cur=root
        precursor=None
        result=[]
        while cur!=None:
            if cur.left==None:
                result.append(cur.val)
                cur=cur.right
            else:
                precursor=cur.left
                while precursor.right!=None and precursor.right!=cur:
                    precursor=precursor.right
                if precursor.right==None:
                    precursor.right=cur
                    result.append(cur.val)                                  #The place of this statement is the only difference.
                    cur=cur.left
                else:
                    precursor.right=None
                    cur=cur.right
        return result
