class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0                                                                 #Use a pointer pointing to the first number which is not popped yet in popped list.
        for x in pushed:                                                      #Traverse pushed and push each number in stack.
            stack.append(x)
            while i < len(popped) and stack and stack[-1] == popped[i]:       #If current stack is not empty and stack pop equals the first not popped number, pop stack and move pointer to next.
                stack.pop()
                i += 1
        return i == len(popped)                                               #If pointer reaches the end of popped, the sequence is valid.
