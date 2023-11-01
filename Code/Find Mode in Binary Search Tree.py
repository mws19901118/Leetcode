# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BST:                                                                                        #Inorder Morris traversal iterator.
    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.right_most = None

    def hasNext(self) -> bool:
        return self.curr

    def next(self) -> int:
        if not self.curr.left:
            temp = self.curr
            self.curr = self.curr.right
            return temp.val
 
        self.right_most = self.curr.left
 
        while self.right_most.right and self.right_most.right != self.curr:
            self.right_most = self.right_most.right
        if not self.right_most.right:
            self.right_most.right = self.curr
            self.curr = self.curr.left
        else:
            self.right_most.right = None
            temp = self.curr
            self.curr = self.curr.right
            return temp.val
 
        return self.next()

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        bst = BST(root)                                                                            #Initialize an inorder Morris traversal iterator.
        modes = []
        maxCount = 0                                                                               #Max count of any number.
        lastValue, count = None, 0                                                                 #Initialize last value and its count.
        while bst.hasNext():                                                                       #Traverse BST.
            x = bst.next()
            if x != lastValue:                                                                     #If x is not same as lastValue, reset lastValue and count.
                lastValue = x
                count = 0
            count += 1                                                                             #Increase count.
            if count >= maxCount:                                                                  #If count >= maxCount, find a potential mode.
                if count > maxCount:                                                               #If count > maxCount, reset modes and update maxCount.
                    modes.clear()
                    maxCount = count
                modes.append(x)                                                                    #Add x to modes.
        return modes
