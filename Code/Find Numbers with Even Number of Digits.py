class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not len(str(x)) & 1 for x in nums)      #Convert each number to string and check if the length is even.
