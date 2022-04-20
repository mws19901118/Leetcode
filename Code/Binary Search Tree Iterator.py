# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []                                                     #Store the path.
        self.curr = root                                                    #Record current node.
        while self.curr.left:                                               #Find the leftmost node.
            self.stack.append(self.curr)
            self.curr = self.curr.left
    
    def next(self) -> int:
        result = self.curr.val                                              #Buffer current value.
        if self.curr.right:                                                 #If self.curr has right child, set self.curr to be the leftmost node in its right subtree, and push the path to self.stack.
            self.curr = self.curr.right
            while self.curr.left is not None:
                self.stack.append(self.curr)
                self.curr = self.curr.left
        elif self.stack:                                                    #If current node does not have right child and self.stack is not empty, pop item as current node if self.stack is not empty.
            self.curr = self.stack.pop()
        else:                                                               #Otherwise, set self.curr = None.
            self.curr = None
        
        return result                                                       #Return buffer.

    def hasNext(self) -> bool:
        return self.curr is not None                                        #When iterator comes to the end, self.curr is none.

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
