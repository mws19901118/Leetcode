class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def calculate(start: int, end: int) -> int:                    #Calculate the number of fixed-bound subarrays in nums[start:end + 1] assuming all numbers are within bounds.
            count, last_min, last_max = 0, -1, -1                      #Initialize count and last index of minK and last index of maxK.  
            for i in range(start, end + 1):                            #Traverse nums[start:end + 1].
                if nums[i] == minK:                                    #Update last_min.
                    last_min = i
                if nums[i] == maxK:                                    #Update last_max.
                    last_max = i
                if last_min != -1 and last_max != -1:                  #If both minK and maxK is visited, all subarrays starting in from start to min(last_min, last_max) and ending at i are fixed-bound.
                    count += min(last_min, last_max) - start + 1
            return count

        result, i = 0, 0                                                #Initialize result.
        while i < len(nums):                                            #Traverse nums to find the segment that all numbers are within bounds.
            j = i
            while j < len(nums) and minK <= nums[j] <= maxK:
                j += 1
            result += calculate(i, j - 1)                               #Add the total fixed-bound subarrays for current segment to result.
            i = max(j, i + 1)
        return result
