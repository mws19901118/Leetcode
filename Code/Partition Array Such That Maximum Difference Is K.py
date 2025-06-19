class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()                                              #Sort nums.
        result, i = 0, 0                                         #Initialize result and a pointer,
        while i < len(nums):                                     #Traverse nums.
            j = i
            while j < len(nums) and nums[j] <= nums[i] + k:      #Find the rightmost j so that x - nums[i] <= k for each number x in nums[i:j].
                j += 1
            result += 1                                          #Group nums[i:j] in one partition.
            i = j                                                #Move i to j.
        return result
