class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []                                    #Use stack to store de-duped letters.
        for x in s:                                   #Traverse s.
            if stack and stack[-1] == x:              #If current letter equals last letter in stack, pop stack.
                stack.pop()
            else:                                     #Otherwise, append x to stack.
                stack.append(x)
        return "".join(stack)                         #Join the stack and return.
