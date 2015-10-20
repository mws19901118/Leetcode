# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def transform(num,start,end,node):
    mid=(start+end)/2                                 #Because num is in ascending order, the index of value of node should be the mean of start and end.
    node.val=num[mid]
    if start<mid:                                     #Mid is larger than start means that node has left child.
        node.left=TreeNode(-1)                        #Initialize the left child of node.
        transform(num, start, mid-1, node.left)       #Construct the BST whose root is the left child of node. 
    if end>mid:                                       #Mid is smaller than end means that node has right child.
        node.right=TreeNode(-1)                       #Initialize the right child of node.
        transform(num, mid+1, end, node.right)        #Construct the BST whose root is the right child of node. 

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length=len(num)
        root=TreeNode(-1)                             #Initialize root.
        if length==0:
            return None
        transform(num, 0, length-1, root)
        return root
        
