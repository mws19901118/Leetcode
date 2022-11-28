class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()                                                       #Sort nums.
        maxSum = -1
        for i, x in enumerate(nums):                                      #Traverse nums.
            index = bisect_left(nums, k - x, i + 1, len(nums)) - 1        #Binary search the index to insert k - x in nums[i + 1].
            if index != i:                                                #If index is greater than i, update maxSum if necessary.
                maxSum = max(maxSum, x + nums[index])
        return maxSum                                                     #Return maxSum.
