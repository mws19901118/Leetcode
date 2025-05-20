class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)            #Initialize overall impact of queryies on each index.
        for l, r in queries:                    #Traverse queries.
            diff[l] += 1                        #Increase diff[l].
            diff[r + 1] -= 1                    #Decrease diff[r + 1].
        s = 0                                   #Initialize s representing max decrease of each index.
        for i, x in enumerate(nums):            #Traverse nums.
            s += diff[i]                        #Increase diff[i] to s.
            if s < x:                           #If s < x, we cannot decrease nums[i] to 0, so return false.
                return False
        return True                             #Return true.
