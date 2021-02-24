class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]                                 #Use a stack to store the score of each level of left parenthesis so far, initally it's 0.
        for x in S:                                 #Traverse S.
            if x == '(':                            #If x is '(', append 0 to stack.
                stack.append(0)
            else:
                y = stack.pop()                     #Otherwise, pop stack to get score of cureent level.
                stack[-1] += y * 2 if y else 1      #If it's 0, nothing is in this '()', so add 1 to upper level; otherwise, add y * 2 to upper level, '(A)' situation.
        return stack[0]                             #Return the only value in stack.
