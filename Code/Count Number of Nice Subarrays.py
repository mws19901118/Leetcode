class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        firstIndex = {0: -1}                                                              #For each count of odd numbers from beginning, store the first index of the count; initially it is -1 for 0.
        oddCount, result = 0, 0                                                           #Initialize odd number count and result.
        for i, x in enumerate(nums):                                                      #Traverse nums.
            if x & 1:                                                                     #If x is odd, increase odd count and set the index.
                oddCount += 1
                firstIndex[oddCount] = i
            if oddCount >= k:                                                             #If there are at least k odd numbers from beginning, then every substring starting in nums[firstIndex[oddCount - k]:firstIndex[oddCount - k + 1]] and ending at current character will have k odd numbers.
                result += firstIndex[oddCount - k + 1] - firstIndex[oddCount - k]
        return result
