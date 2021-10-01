class Solution:
    def DP(self, nums: List[int], mask: int, x: int, target: int, cache: dict) -> bool:     #Find if current remain numbers in nums can form a set whose sum is x. Also, target is the equal sum of k subsets and cache memorizes visited results.
        if (mask, x) in cache:                                                              #If (mask, x) is in cache, return cache[(mask, x)].
            return cache[(mask, x)]
        if mask == 0:                                                                       #If mask == 0, all the elements have been used, and we need to see whether x == 0. If it is, we have found a way to epartition nums to k subsets with equal sum.
            return x == 0
        elif x == 0:                                                                        #If x == 0, but mask != 0, we found a subset whose sum equals target. We need to keep searching until all the number in the nums are used.
            return self.DP(nums, mask, target, target, cache)
        result, bit = False, 1                                                              #Initialize result to false and bit to 1.
        for i in range(len(nums)):                                                          #Traverse nums.
            if mask & bit and nums[i] <= x:                                                 #If mask & bit(which means nums[i] is not used) and nums[i] <= x, we can add nums[i] into current set.
                result |= self.DP(nums, mask ^ bit, x - nums[i], target, cache)             #Keep searching and update result.
                if result:                                                                  #If result is true, break./
                    break
            bit <<= 1                                                                       #Left shift bit.
        cache[(mask, x)] = result                                                           #Set result to cache[(mask, x)].
        return cache[(mask, x)]                                                             #Return cache[(mask, x)].
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        q, r = divmod(sum(nums), k)                                                         #Calculate the target sum of each subset.
        if r != 0 or any(x > q for x in nums):                                              #If the sum(nums) cannot be divided by r or there is any number larger than target sum, we cannot partition nums to k subsets with equal sum, so return false directly.
            return False
        nums.sort(reverse = True)                                                           #Sort nums in descending order.
        return self.DP(nums, 2 ** len(nums) - 1, q, q, {})                                  #Return the result of DP.
