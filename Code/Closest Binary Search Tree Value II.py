# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getPredecessor(self, predecessor, target):                #Get the predecessor of target value.
        t = TreeNode(target)
        while len(predecessor) != 0:                              #While stack is not empty, pop stack until reach a value smaller than target.
            t = predecessor.pop()
            if t.val < target:
                break
        if t.val >= target:                                       #If can not find, return target value to indicate that it's the smallest one in the BST.
            return target
        p = t.val                                                 #Otherwise, record the answer node.
        t = t.left                                                #Push the path from the left child of answer node to its rightmost decendent to the stack.
        while t != None:
            predecessor.append(t)
            t = t.right
        return p                                                  #Return answer value.
        
    def getSuccessor(self, successor, target):                    #Get the successor of target value.
        t = TreeNode(target)
        while len(successor) != 0:                                #While stack is not empty, pop stack until reach a value larger than target.
            t = successor.pop()
            if t.val > target:
                break
        if t.val <= target:                                       #If can not find, return target value to indicate that it's the largest one in the BST.
            return target
        s = t.val                                                 #Otherwise, record the answer node.
        t = t.right                                               #Push the path from the right child of answer node to its leftmost decendent to the stack.
        while t != None:
            successor.append(t)
            t = t.left
        return s                                                  #Return answer value.
        
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        result = []
        predecessor = []                                          #Store the path for predecessor.
        successor = []                                            #Store the path for successor.
        while root != None:                                       #Append the path to both stack until reaching the target or comming to an end.
            predecessor.append(root)
            successor.append(root)
            if root.val == target:                                #If reach the target, directly append it to result and decrease k by 1.
                result.append(int(target))
                k -= 1
                if root.left != None:                             #If target has left child, push the path from the left child to its rightmost decendent to the predecessor stack.
                    t = root.left
                    while t != None:
                        predecessor.append(t)
                        t = t.right
                if root.right != None:                            #If target has right child, push the path from the right child to its leftmost decendent to the successor stack.
                    t = root.right
                    while t != None:
                        successor.append(t)
                        t = t.left
                break
            elif root.val > target:
                root = root.left
            else:
                root = root.right

        nextPredecessor = True                                    #Indicates the next value to get is the predecessor.
        nextSuccessor = True                                      #Indicates the next value to get is the successor.
        noNewPredecessor = False                                  #Indicates there is no more predecessors, i.e. reaching the smallest value of BST.
        noNewSuccessor = False                                    #Indicates there is no more successor, i.e. reaching the largest value of BST.
        p = target                                                #Record the current value which is most closely larger than target.
        s = target                                                #Record the current value which is most closely smaller than target.
        while k > 0:
            if nextPredecessor:
                newp = self.getPredecessor(predecessor, p)        #Get the next predecessor
                if newp == p:                                     #Reach the smallest value of BST.
                    noNewPredecessor =True
                else:
                    p = newp
            if nextSuccessor:
                news = self.getSuccessor(successor, s)            #Get the next successor
                if news == s:                                     #Reach the largest value of BST.
                    noNewSuccessor = True
                else:
                    s = news
            if noNewPredecessor:                                  #If reach the smallest value of BST, can only append successor to result now.
                result.append(s)
                nextSuccessor = True
            elif noNewSuccessor:                                  #If reach the largest value of BST, can only append predecessor to result now.
                result.append(p)
                nextPredecessor = True
            else:
                if abs(p - target) < abs(s - target):             #Append the closer value of predecessor and successor to result and get next value in the opposite direction in next iteration.
                    result.append(p)
                    nextSuccessor = False
                    nextPredecessor = True
                else:
                    result.append(s)
                    nextPredecessor = False
                    nextSuccessor = True
            k -= 1
        return result
