class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        l = len(preorder)
        stack = []                                            #Use stack to store the descending sequence we have before current number.
        lowerbound = -0x80000000                              #Record the lower bound of current number.
        for i in range(l):
            while stack != [] and stack[-1] <= preorder[i]:   #For each number, find its possible parent, i.e. the first element(if any) in stack which is larger than current element.
                lowerbound = stack.pop()                      #To maintain a BST, current number should be larger than all the popped numbers, so update lower bound every time.
            if preorder[i] <= lowerbound:                     #Judge if it's valid.
                return False
            stack.append(preorder[i])                         #Append current number to stack.
        return True                                           #If no conflicts found, return true.
