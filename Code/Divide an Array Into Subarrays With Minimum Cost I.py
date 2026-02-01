class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minValue, secondMinValue = inf, inf            #Find the min value and second min value in nums[1:].
        for x in nums[1:]:
            if x < minValue:
                secondMinValue = minValue
                minValue = x
            elif x < secondMinValue:
                secondMinValue = x
        return nums[0] + minValue + secondMinValue     #Sum up with nums[0] then return.
