class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(index: int, stack: List[int]) -> None:
            if index == len(nums):                                              #If index reaches the end of nums, append the deep copy of stack to result.
                result.append(deepcopy(stack))
                return
            backtrack(index + 1, stack)                                         #Keep backtracking.
            stack.append(nums[index])                                           #Append nums[index] to stack.
            backtrack(index + 1, stack)                                         #Keep backtracking.
            stack.pop()                                                         #Pop stack.

        result = []
        backtrack(0, [])                                                        #Start backtracking.
        return result
