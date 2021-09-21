class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, result = 0, 0                    #Intialize count and result.
        for x in nums:                          #Traverse nums.
            if x == 0:                          #If x == 0, set count to 0.
                count = 0
            else:                               #Otherwise, increase count and update result.
                count += 1
                result = max(result, count)
        return result
