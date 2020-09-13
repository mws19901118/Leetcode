class Solution:
    def backtracking(self, k: int, n: int, stack: List[int], s: int, nums: List[int], result: List[List[int]]) -> None:
        if s >= n or len(stack) >= k:                                                   #If current sum is equal to or larger than n or current stack length is equal to or larger than k, stop backtracking.
            if s == n and len(stack) == k:                                              #If current sum is n and current stack length is k, we found a valid combination, deep copy stack into result.
                result.append(copy.deepcopy(stack))
            return
        for i, x in enumerate(nums):                                                    #Traverse from remaining nums.
            stack.append(x)                                                             #Push to stack.
            self.backtracking(k, n, stack, s + x, nums[i + 1:], result)                 #Backtrack next level.
            stack.pop()                                                                 #Pop from stack.
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(k, n, [], 0, [1, 2, 3, 4, 5, 6, 7, 8, 9], result)             #Backtrack.
        return result
