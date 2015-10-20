# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):                        #Do the binary tree level order traverse.
        result=[]
        if root==None:
            return result
        current=[root]
        thenext=[]
        while current!=[]:
            for i in range(len(current)):
                if current[i].left!=None:
                    thenext.append(current[i].left)
                if current[i].right!=None:
                    thenext.append(current[i].right)
                if i==len(current)-1:
                    result.append(current[i].val)         #Append value of the last node of each level to result.
            current=thenext
            thenext=[]
        return result
