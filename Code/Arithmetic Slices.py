class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result, count = 0, 0                                                                        #Initialize result and count of arithmetic subarrays ending at current index.
        for i in range(2, len(nums)):                                                               #Traverse nums from index 2.
            count = count + 1 if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] else 0          #Increase count by 1 if nums[i - 2:i + 1] is a arithmetic subarray; otherwise, set count to 0.
            result += count                                                                         #Add count to result
        return result
