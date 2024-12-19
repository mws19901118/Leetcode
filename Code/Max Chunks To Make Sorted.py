class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []                                    #Use a stack to store the max value in each chunk.
        for x in arr:                                 #Traverse arr.
            max_v = x                                 #Initialize max value for current chunk.
            while stack and stack[-1] > x:            #While stack is not empty and the top of stack is greater than current number, current number should merge with the chunk on top of stack.
                max_v = max(max_v, stack.pop())       #Pop stack and update max value.
            stack.append(max_v)                       #Append max value to stack.
        return len(stack)                             #Return the length of stack.
