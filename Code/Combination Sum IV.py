class Solution:
    def dp(self, nums: List[int], cache: dict, target: int) -> int:
        if target in cache:                                                   #If target is already in cache, return cache[target].
            return cache[target]
        count = 0                                                             #Count the combination sum of target.
        for x in nums:                                                        #Traverse nums.
            if x > target:                                                    #If x is already greater than 0, stop.
                break
            else:                                                             #Otherwise, add the combination sum of target - x to count.
                count += self.dp(nums, cache, target - x)
        cache[target] = count                                                 #Add count to cache for target.
        return count                                                          #Return count.
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()                                                           #Sort nums.
        return self.dp(nums, {0: 1}, target)                                  #Start dp with memorization and the combination sum of 0 is 1.
