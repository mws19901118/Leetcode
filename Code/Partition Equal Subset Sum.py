class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)                                                            #Get the sum of nums.
        if target & 1:                                                                #If sum is odd, nums cannot be partitioned equally, return false.
            return False
        target >>= 1                                                                  #Divide the sum by 2 and target is the sum of each subset.
        dp = [True] + [False] * target                                                #Initialize DP list, dp[i] means if a subset whose sum is i can be partitioned.
        for x in nums:                                                                #Iterate over nums.
            dp = [dp[s] or (s >= x and dp[s - x]) for s in range(target + 1)]         #For each value s from 0 to target, a subset can be partitioned at that value if a partition whose value is s - x can be partitioned.
            if dp[target]:                                                            #If can partition such subset, return true.
                return True
        return False                                                                  #If cannot partition, return false.
