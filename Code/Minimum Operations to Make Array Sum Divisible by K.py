class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k        #Return the remainder of overall sum divided by k.
