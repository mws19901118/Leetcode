class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []                                                        #Use stack to store characters in final result.
        for x in s:                                                       #Traverse s.
            if len(stack) >= 2 and stack[-1] == x and stack[-2] == x:     #If stack has at least 2 characters and current character equals to the top 2 characters of stack, skip.
                continue
            stack.append(x)                                               #Append x to stack.
        return "".join(stack)                                             #Join stack and return.
