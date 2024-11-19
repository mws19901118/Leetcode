class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        indexes = {}                                                                    #Store the last index of all the number in sliding window.
        start, s, result = 0, 0, 0                                                      #Initialize start of sliding window, sum of sliding window and result.
        for i, x in enumerate(nums):                                                    #Traverse nums.
            new_start = max(start, (indexes[x] if x in indexes else i - k) + 1)         #Calculate the new start of sliding window. indexes[x] + 1 if x is already seen, or i - k + 1 if not, or previous start if neither of these is greater than previous start.
            while start < new_start:                                                    #Move to new_start.
                indexes.pop(nums[start])                                                #Pop nums[start] from indexes.
                s -= nums[start]                                                        #Substract nums[start] from sum.
                start += 1
            indexes[x] = i                                                              #Set indexes[x] to i.
            s += x                                                                      #Add x to s.
            if len(indexes) == k:                                                       #If there are k numbers in sliding window, update result if necessary.
                result = max(result, s)
        return result
