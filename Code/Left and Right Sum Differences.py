class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0                                          #Initialize left sum.
        s = sum(nums)                                     #Sum up nums.
        result = []
        for x in nums:                                    #Traverse nums.
            result.append(abs(s - left - x - left))       #Right sum is s - left - x.
            left += x                                     #Update left.
        return result
