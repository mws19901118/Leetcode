# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def count(self,root,dict):                                                        #Count the number of nodes in a BST and store it in a dict.
        if root==None:                                                                #If root is none, return 0.
            return 0
        else:                                                                         #Otherwise, return the number of nodes in the left child of root plus the number of nodes in the right child of root plus 1.
            dict[root]=self.count(root.left, dict)+self.count(root.right, dict)+1
            return dict[root]
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        dict={}
        n=self.count(root,dict)                                                       #Count the number of nodes in root.
        if root.left!=None:                                                           #Use l to store the number of nodes in the left child of root.If the left child of root is not none, fetch the number from dict; otherwise, it is 0.
            l=dict[root.left]
        else:
            l=0
        if l==k-1:                                                                    #If the value of root is exactly the k-th smallest number, return it.
            return root.val
        elif l<k-1:                                                                   #If l is smaller than k-1, find the (k-l-1)-th smallest number in the right child of root. Because k is always valid, we don't have to worry about that root.right is none.
            return self.kthSmallest(root.right, k-l-1)
        else:                                                                         #If l is greater than k, find the k-thsmallest number in the left child of root. Because k is always valid, we don't have to worry about that root.left is none.
            return self.kthSmallest(root.left, k)
