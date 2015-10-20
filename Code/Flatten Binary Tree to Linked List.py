# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self,root):
        def transform(root):
            if root==None:
                return
            if root.left==None and root.right==None:                    #If current node is leaf, return current node.
                return root
            elif root.left!=None and root.right==None:                  #If current node only has left child, recursively process its left child, point its right pointer to left child, point its left pointer to None and return the last node below the left child.
                temp= transform(root.left)
                root.right=root.left
                root.left=None
                return temp
            elif root.left==None and root.right!=None:                  #If current node only has right child, recursively process its right child and return the last node below the right child.
                temp=transform(root.right)
                return temp
            else:                                                       #If current node has both child, recursively process both child, connect the last node below the left child and the right child, point its right pointer to left child, point its left pointer to None and return the last node below the right child.
                templ= transform(root.left)
                tempr=transform(root.right)
                templ.right=root.right
                root.right=root.left
                root.left=None
                return tempr

        temp=transform(root)                                            #call the function
