class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []                                                      #Use a stack to store digits.
        for x in num:                                                   #Traverse nums.
            while stack and stack[-1] > x and k:                        #While stack is not empty and top of stack is greater than x and k is larger than 0, pop stack to remove current digit.
                stack.pop()
                k -= 1
            stack.append(x)                                             #Append x to stack.
        stack = stack[:len(stack) - k]                                  #Remove the last k diigts from stack.
        return str(int("".join(stack))) if stack else "0"               #If stack is not empty, join digits and convert to int then covert back to str to remove leading "0"; otherwise, return "0" directly.
