class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = Counter(nums)                                                                          #Count numbers in nums.
        return all(count[i] == 1 for i in range(1, len(nums) - 1)) and count[len(nums) - 1] == 2       #Return true if count[i] == 1 for all i from 1 to len(nums) - 2 and count[len(nums) - 1] == 2.
