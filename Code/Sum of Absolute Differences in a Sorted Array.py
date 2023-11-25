class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = [sum(x - nums[0] for x in nums)]                                                  #Calculate summation of absolute differences for nums[0].
        for i in range(1, len(nums)):                                                              #Traverse the rest of nums.
            result.append(result[-1] + (nums[i] - nums[i - 1]) * (i * 2 - len(nums)))              #Based on result of previous number, result of current number will increse (nums[i] - nums[i - 1]) * (i - 1) and decrease (nums[i] - nums[i - 1]) * (len(nums) - 1 - i).
        return result
