class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSumRemainder = {0: -1}                    #Store the prefix sum remainder after mod k in dictionary. Initially the remainder is 0 for -1.
        s = 0                                           #Initiialize prefix sum remainder.
        for i, x in enumerate(nums):                    #Traverse nums.
            s = (s + x) % k                             #Calculate new prefix sum remainder.
            if s not in prefixSumRemainder:             #If it is not in prefixSumRemainder, set prefixSumRemainder[s] to i.
                prefixSumRemainder[s] = i
            elif i - prefixSumRemainder[s] >= 2:        #Othwise if i - prefixSumRemainder[s] >= 2, then there is a continuous subarray nums[prefixSumRemainder[s] + 1:i + 1] whose sum is a multiple of k and longer than 2, return true.
                return True
        return False                                    #Return false if not found such subarray.
