class Solution:
    def backtracking(self, nums: List[int], stack: List[int], result:List[List[int]]):
        if not nums:                                                                        #If no more nums, append the deep copy of stack to result.
            result.append(deepcopy(stack))
            return
        stack.append(nums[0])                                                               #Append nums[0] to stack.
        self.backtracking(nums[1:], stack, result)                                          #Keep backtracking.
        stack.pop()                                                                         #Pop stack.
        self.backtracking(nums[1:], stack, result)                                          #Keep backtracking.
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [], result)                                                 #Find all subsets using backtracking.
        return result
