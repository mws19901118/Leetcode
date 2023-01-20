class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()                                                  #Store result in a set.
        stack = []                                                      #Initialize the stack for backtracking.
        def backtrack(index):
            if index == len(nums):                                      #Backtrack reaches end.
                if len(stack) >= 2:                                     #If there are at least 2 elements in stack, convert stack to tuple and add it to result set.
                    result.add(tuple(stack))
                return
            if not stack or stack[-1] <= nums[index]:                   #If stack is empty or top of stack is smaller or equal to nums[index], push nums[index] to stack.
                stack.append(nums[index])
                backtrack(index + 1)                                    #Keep backtracking with nums[index].
                stack.pop()                                             #Pop stack to restore.
            backtrack(index + 1)                                        #Keep backtracking without nums[index].
        backtrack(0)                                                    #Start backtracking from index 0.
        return result                                                   #Return result.
