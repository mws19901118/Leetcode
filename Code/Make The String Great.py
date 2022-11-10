class Solution:
    def makeGood(self, s: str) -> str:
        stack = []                                                                    #Use stack to store characters.
        for x in s:                                                                   #Traverse s.
            if stack and abs(ord(stack[-1]) - ord(x)) == abs(ord('a') - ord('A')):    #If stack is not empty and x is case different with top of stack, pop stack.
                stack.pop()
            else:                                                                     #Otherwise, append x to stack.
                stack.append(x)
        return "".join(stack)                                                         #Join stack and return.
