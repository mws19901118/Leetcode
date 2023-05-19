class Solution:    
    def maxScore(self, nums: List[int]) -> int:
        @cache                                                                                                                              #Cache result.
        def backtrack(mask: int, operation: int) -> int:                                                                                    #Backtrack with current number picking state(represented by mask) and number of operations taken.
            if 2 * operation == len(nums):                                                                                                  #If all numbers are picked, return 0.
                return 0
              
            maxScore = 0                                                                                                                    #Initialize max score.
            for i in range(len(nums)):                                                                                                      #Traverse each number pair in nums.
                for j in range(i + 1, len(nums)):
                    if (mask >> i) & 1 == 1 or (mask >> j) & 1 == 1:                                                                        #If either one is already picked, skip.
                        continue
                    newMask = mask | (1 << i) | (1 << j)                                                                                    #Mark i and j as picked.
                    maxScore = max(maxScore, (operation + 1) * math.gcd(nums[i], nums[j]) + backtrack(newMask, operation + 1))              #Calculate score(current score plus future score) and update max score if necessary.
            return maxScore                                                                                                                 #Return maxScore.

        return backtrack(0, 0)                                                                                                              #Start backtracking from the beginning.
