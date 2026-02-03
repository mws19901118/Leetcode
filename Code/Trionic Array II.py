class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        desendingSubarrays = []                                                #Store the 2 ends of all strictly desending subarray in nums.
        i = 1                                                                  #Traverse from 1 to len(nums) - 1 to populate desendingSubarrays. 
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums) - 1 and nums[j] < nums[j - 1]:
                j += 1
            if j > i + 1:
                desendingSubarrays.append((i, j - 1))
            i = j
        result = -inf
        for s, e in desendingSubarrays:                                        #Traverse desendingSubarrays.
            if nums[s - 1] >= nums[s] or nums[e + 1] <= nums[e]:               #If nums[s - 1] >= nums[s] or nums[e + 1] <= nums[e], current desending array cannot form a trionic array, so skip. 
                continue
            i = s - 1                                                          #Traverse the 1st strictly increaseing subarray backward and find the max strictly increaseing subarray sum ending at nums[s - 1].
            runningSum1, maxSum1 = 0, -inf
            while i >= 0 and nums[i] < nums[i + 1]:
                runningSum1 += nums[i]
                maxSum1 = max(maxSum1, runningSum1)
                i -= 1
            j = e + 1                                                          #Traverse the 2nd strictly increaseing subarray forward and find the max strictly increaseing subarray sum starting at nums[e + 1].
            runningSum2, maxSum2 = 0, -inf
            while j < len(nums) and nums[j] > nums[j - 1]:
                runningSum2 += nums[j]
                maxSum2 = max(maxSum2, runningSum2)
                j += 1
            result = max(result, maxSum1 + maxSum2 + sum(nums[s:e + 1]))       #Current max trionic subarray sum is maxSum1 + maxSum2 + sum(nums[s:e + 1]); update result if necessary.
        return result
