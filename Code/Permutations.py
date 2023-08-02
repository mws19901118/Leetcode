class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack, result = [], []                                                #Initialize stack and result.
        masks = {i : 1 << (i + 1) for i in range(len(nums))}                  #Use bit masks to indicate if each number is already used.
        def backtrack(state: int):                                            #Backtracking with a bit mask of all numbers used.
            if len(stack) == len(nums):                                       #If length of stack is same as length of nums, we found a permutation, so append the copy of stack to result and return.
                result.append(stack.copy())
                return
            for i, x in enumerate(nums):                                      #Traverse nums.
                if state & masks[i]:                                          #If current number is already used, skip.
                    continue
                stack.append(x)                                               #Append x to stack.
                backtrack(state | masks[i])                                   #Keep backtracking with updated state.
                stack.pop()                                                   #Pop stack.
        
        backtrack(0)                                                          #Backtrack from no number used.
        return result
