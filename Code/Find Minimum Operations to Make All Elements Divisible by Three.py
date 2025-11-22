class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(int(x % 3 > 0) for x in nums)    #For any number not divisible by 3, add 1 or minus 1 to make it divisible by 3.
