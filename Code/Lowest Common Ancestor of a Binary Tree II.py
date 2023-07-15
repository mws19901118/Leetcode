# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(root: 'TreeNode') -> ('TreeNode', bool, bool):                                #Traverse current subtree to get the lca in current subtree and if current subtree has p and if current subtree has q.
            if not root:                                                                           #If root is none, return (none, false, false).
                return None, False, False
            lcaInLeft, pInLeft, qInLeft = traverse(root.left)                                      #Get the result of left subtree.
            if lcaInLeft:                                                                          #If lca is in left subtree, return (lcaInLeft, true, true).
                return lcaInLeft, True, True
            lcaInRight, pInRight, qInRight = traverse(root.right)                                  #Get the result of right subtree.
            if lcaInRight:                                                                         #If lca is in right subtree, return (lcaInRight, true, true).
                return lcaInRight, True, True
            hasP, hasQ = pInLeft or pInRight or root == p, qInLeft or qInRight or root == q        #If p is in either subtree or is root, current subtree has p; if q is in either subtree or is root, current subtree has q.
            return (root, True, True) if hasP and hasQ else (None, hasP, hasQ)                     #If current subtree has both p and q, root is the lca, so return (root, true, true); otherwise return (none, hasP, hasQ).

        return traverse(root)[0]                                                                   #Return the first element of the result of traversing from root.
