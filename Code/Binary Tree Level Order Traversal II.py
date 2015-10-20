# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        result=[]
        if root==None:
            return result
        current=[root]
        thenext=[]
        while current!=[]:
            temp=[]
            for i in current:
                temp.append(i.val)
                if i.left!=None:
                    thenext.append(i.left)
                if i.right!=None:
                    thenext.append(i.right)
            current=thenext
            thenext=[]
            result.append(temp)
        result.reverse()                        #Reverse the result. The rest is same as Binary Tree Level Order Traversal.
        return result
