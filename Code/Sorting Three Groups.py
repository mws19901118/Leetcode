class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        @cache                                                            #Cache result.
        def dp(i: int, prev: int):                                        #DP to calculate the min operations needed for nums[i:] with given prev value.
            if i == len(nums):                                            #If i reaches the end, return 0.
                return 0
            if nums[i] == prev:                                           #If nums[i] == prev, nums[:i + 1] is still not desending, so no operation needed and continue dp.
                return dp(i + 1, prev)
            elif nums[i] < prev:                                          #If nums[i] < prev, we have to update nums[i[ which needs 1 operation, then continue dp.
                return dp(i + 1, prev) + 1
            else:                                                         #Otherwise, return the min value of continuing dp with no operation or change nums[i] to prev.
                return min(dp(i + 1, nums[i]), dp(i + 1, prev) + 1)
        return dp(0, 1)                                                   #Start dp from index 0 with min value 1.
