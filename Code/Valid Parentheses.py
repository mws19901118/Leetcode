class Solution:
    def isValid(self, s: str) -> bool:
        parentheseDict = {')': '(', ']': '[', '}': '{'}         #Store the valid matches.
        stack = []
        for x in s:
            if x in parentheseDict.values():                    #If x is left parenthesis, append x into stack.
                stack.append(x)
            elif stack and stack[-1] == parentheseDict[x]:      #If the top of stack matches x, pop stack.
                stack.pop()
            else:                                               #Otherwise s is not valid, return false directly.
                return False
        return not stack                                        #If stack is empty, the s is valid.
