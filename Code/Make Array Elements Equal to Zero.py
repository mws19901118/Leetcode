class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)                                    #Calculate the total sum of nums.
        prefixSum, result = 0, 0                         #Initialize prefix sum and result.
        for x in nums:                                   #Traverse nums.
            if x:                                        #If x is positive, update prefix sum and continue.
                prefixSum += x
                continue
            result += int(prefixSum == s >> 1)           #If the prefix sum so far is s // 2, we can choose current index and go right, eventually all the numbers are 0 and the process stops at the right end.
            result += int(s - prefixSum == s >> 1)       #If the other half sum is s // 2, we can choose current index and go left, eventually all the numbers are 0 and the process stops at the left end.
        return result
