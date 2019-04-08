class Solution:
    def backtracking(self, nums, cache, target):                            #Return the count of possible combinations for a target.
        if target == 0:                                                     #If target is 0, return 1.
            return 1
        elif target > 0:                                                    #If target is larger than 0 and target is in cache, return target[cache]
            if target in cache:
                return cache[target]
            count = 0                                                       #Initialize count.
            for x in nums:                                                  #Traverse through nums and substract x from target, then backtracking.
                count += self.backtracking(nums, cache, target - x)         #Add up each result of backtracking.
            cache[target] = count                                           #Add count to cache for current target.
            return count                                                    #Return count.
        else:                                                               #If target is smaller than 0, return 0.
            return 0
            
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.backtracking(nums, {}, target)                          #Backtracking.
