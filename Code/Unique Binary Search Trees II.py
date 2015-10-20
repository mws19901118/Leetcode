# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        def constructTrees(a,b):                                  #Construct a BST values a...b.
            if a>b:
                return [None]
            else:
                total=[]                                          #Record current list of tree nodes.
                for i in range(a,b+1):
                    leftT=constructTrees(a,i-1)                   #Construct the left child of current root.
                    rightT=constructTrees(i+1,b)                  #Construct the right child of current root.
                    for t1 in leftT:
                        for t2 in rightT:
                            root=TreeNode(i)                      #New current root.
                            root.left=t1                          #Link current root with its left child.
                            root.right=t2                         #Link current root with its right child.
                            total.append(root)                    #Append current root to the list.
                return total
        return constructTrees(1, n)
