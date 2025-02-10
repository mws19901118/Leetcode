class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []                #Store characters in a stack.
        for x in s:               #Traverse s.
            if x.isdigit():       #If current character is digit, pop the stack.
                stack.pop()
            else:                 #Otherwise, append current character to stack.
                stack.append(x)
        return "".join(stack)     #Join stack and return.
