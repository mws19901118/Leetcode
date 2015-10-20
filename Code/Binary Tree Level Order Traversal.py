# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result=[]
        if root==None:
            return result
        current=[root]                                  #Store current level of nodes.
        thenext=[]                                      #Store next level of nodes.
        while current!=[]:                              #If current is empty, break.
            temp=[]                                     #Store the value of nodes.
            for i in current:
                temp.append(i.val)                      #Add value to temp.
                if i.left!=None:                        #If node has left child, add it to the next.
                    thenext.append(i.left)
                if i.right!=None:                       #If node has right child, add it to the next.
                    thenext.append(i.right)
            current=thenext                             #Use next level to replace current level.
            thenext=[]                                  #Clear the next.
            result.append(temp)                         #Add temp to result.
        return result
