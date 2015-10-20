# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        cur=root
        precursor=None
        self.result=[]
        while cur!=None:                                                #Inorder traversal.
            if cur.left==None:
                self.result.append(cur.val)
                cur=cur.right
            else:
                precursor=cur.left
                while precursor.right!=None and precursor.right!=cur:
                    precursor=precursor.right
                if precursor.right==None:
                    precursor.right=cur
                    cur=cur.left
                else:
                    precursor.right=None
                    self.result.append(cur.val)
                    cur=cur.right
        self.result.reverse()                                           #Reverse the list to let the smallest number place in the rear.

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.result)!=0:
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        return self.result.pop()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
