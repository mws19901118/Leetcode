class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, count, i = 1, 0, 0                        #Initialize the smallest missing number, total count of patches and the pointer which traverses in nums. 
        while miss <= n:                                #Iterate while miss is not be greater than n.
            if i < len(nums) and nums[i] <= miss:       #If nums[i] is smaller than or equal to miss, we can build all the sum in [1, miss + nums[i]).
                miss += nums[i]
                i += 1
            else:                                       #Otherwise, we have to add a number at miss. Then we can build all the sum in [1, 2 * miss).
                miss *= 2
                count += 1
        return count
