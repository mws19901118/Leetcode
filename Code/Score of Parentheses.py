class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]                                 #Use a stack to store the score of each level of left parenthesis so far, initally it's 0.
        for x in s:                                 #Traverse s.
            if x == '(':                            #If x is '(', append 0 to stack.
                stack.append(0)
            else:
                y = stack.pop()                     #Otherwise, pop stack.
                stack[-1] += y * 2 if y else 1
        return stack[0]
