class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []                                          #Initialize a stack.
        for x in ops:                                       #Traverse ops.
            if x == "C":                                    #Handle "C".
                stack.pop()
            elif x == "D":                                  #Handle "D".
                stack.append(stack[-1] * 2)
            elif x == "+":                                  #Handle "+"
                stack.append(stack[-1] + stack[-2])
            else:                                           #Append to stack if it's score.
                stack.append(int(x))
        return sum(stack)                                   #Sum up scores in stach and return.
