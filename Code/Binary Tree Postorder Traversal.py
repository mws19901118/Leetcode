# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root==None:
            return []
        end=TreeNode(-1)
        stack=[]                                            #record the path
        stack.append(end)
        result=[]
        while root!=end:
            if root.left!=None:                             #current root has left child
                temp=root.left
                root.left=None
                stack.append(root)                          #push current root into stack
                root=temp                                   #new root=left child
            else:
                if root.right!=None:                        #current root has right child
                    temp=root.right
                    root.right=None
                    stack.append(root)                      #push current root into stack
                    root=temp                               #new root=right child
                else:                                       #current root has no child
                    result.append(root.val)                 #add current root to result
                    root=stack.pop()                        #pop path stack
        return result
