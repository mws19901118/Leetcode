# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root==None:
            return 0
        lh=0                                                                    #Record the height of left tree(tree whose root is left child of current root).
        rh=0                                                                    #Record the height of right tree(tree whose root is right child of current root).
        l=root
        r=root
        while l.left!=None:                                                     #Because it's complete tree, the length of the left most branch is the height of left tree.
            l=l.left
            lh+=1
        while r.right!=None:                                                    #Because it's complete treem the length of the right most branch is the height of right tree.
            r=r.right
            rh+=1
        if lh==rh:                                                              #If left height equals right height, it's a perfect tree and return 2^(lh+1)-1.
            return pow(2,lh+1)-1
        else:                                                                   #If it's not a perfect tree, calculate number of nodes recursibely.
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
