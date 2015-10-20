# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        cur=root                                                        #Record current node.
        precursor=None                                                  #Record the precursor node in binary search tree.
        pre=TreeNode(-0xFFFFFFFF)                                       #Record previous node
        first=None                                                      #Record the first node to be swapped.
        second=None                                                     #Record the second node to be swapped.
        while cur!=None:                                                #Use Morris Inorder Traversal.
            if cur.left==None:                                          #If left child of current node is none, it means we are now traversing current node.
                if cur.val<pre.val:                                     #Check if value of current node is smaller than that of previous node.
                    if first==None:                                     #If first is none, let first be previous node and second be current node.
                        first=pre
                        second=cur
                    else:                                               #If first is not none, let second be current node.
                        second=cur
                pre=cur                                                 #Replace previous node with current node.
                cur=cur.right                                           #Replace current node with its right child.
            else:                                                       #If left child of current node is not none, find the precursor node.
                precursor=cur.left
                while precursor.right!=None and precursor.right!=cur:   #The precursor node should be the rightmost node in the left child of current node.
                    precursor=precursor.right
                if precursor.right==None:                               #If right child of precursor node is none, it means current node has not been traversed. 
                    precursor.right=cur                                 #Link precuresor node with current node.
                    cur=cur.left                                        #Replace current node with the left child of current node.
                else:                                                   #If right child of precursor node is not none, it means we are now traversing current node.                                  
                    if cur.val<pre.val:                                 #Check if value of current node is smaller than that of previous node.
                        if first==None:                                 #If first is none, let first be previous node and second be current node.
                            first=pre
                            second=cur
                        else:                                           #If first is not none, let second be current node.
                            second=cur
                    precursor.right=None                                #Recover the tree structure.
                    pre=cur                                             #Replace previous node with current node.
                    cur=cur.right                                       #Replace current node with its right child.
        temp=first.val                                                  #Swap the value of first and that of second.
        first.val=second.val
        second.val=temp
        return root
