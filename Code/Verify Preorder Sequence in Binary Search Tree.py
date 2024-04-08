class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []                                                      #Use stack to store the descending sequence we have before current number.
        lowerbound = 1                                                  #Record the lower bound of current number.
        for x in preorder:
            if x < lowerbound:                                          #Judge if it's valid.
                return False
            while stack and stack[-1] < x:                              #For each number, find its possible parent, i.e. the first element(if any) in stack which is larger than current element.
                lowerbound = max(lowerbound, stack.pop())               #To maintain a BST, current number should be larger than all the popped numbers, so update lower bound every time.
            stack.append(x)                                             #Append current number to stack.
        return True                                                     #If no conflicts found, return true.
