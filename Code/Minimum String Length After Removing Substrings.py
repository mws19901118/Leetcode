class Solution:
    def minLength(self, s: str) -> int:
        stack = []                                                                                #Store letters in stack.
        for x in s:                                                                               #Traverse s.
            if stack and ((x == 'B' and stack[-1] == 'A') or (x == 'D' and stack[-1] == 'C')):    #If stack is not empty and either x is 'B' and top of stack is 'A' or x is 'D' and top of stack is 'C', pop stack and continue.
                stack.pop()
                continue
            stack.append(x)                                                                       #Append x to stack.
        return len(stack)                                                                         #Return the length of stack.
