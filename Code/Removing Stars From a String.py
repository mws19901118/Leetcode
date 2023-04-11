class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for x in s:                   #Traverse s.
            if x != '*':              #Append to stack if is not '*'.
                stack.append(x)
            else:                     #Pop stack if is '*'.
                stack.pop()
        return "".join(stack)         #Join stack and return.
