class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []                                  #Use stack to store characters and its count.
        for x in s:                                 #Traverse s.
            if not stack or stack[-1][0] != x:      #If stack is empty or the character at the top of stack is not x, append x and 1 to stack.
                stack.append([x, 1])
            else:                                   #Otherwise, increase 1 to the count at the top of stack.
                stack[-1][1] += 1
                if stack[-1][1] == k:               #If the count reaches k, pop stack.
                    stack.pop()
        result = ""                                 #Restore duduped string from stack.
        for x, count in stack:
            result += x * count
        return result                               #Return result.
