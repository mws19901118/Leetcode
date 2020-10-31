class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:                                                                          #If nums is empty, return 0.
            return 0
        length, count = [1] * len(nums), [0] * len(nums)                                      #Initialize 2 lists for dynamic programming. One for max length of increasing subsequence, the other one for its count.
        for i, x in enumerate(nums):                                                          #Traverse through nums.
            for j, y in enumerate(nums[:i]):                                                  #Calculete the max length of increasing subsequence ending at i.
                if y < x:                                                                     #If y < x, length[i] = max(length[i], length[j] + 1).
                    length[i] = max(length[i], length[j] + 1)
            for j, y in enumerate(nums[:i]):                                                  #Calculate the count of max length increasing subsequence ending at i.
                if y < x and length[j] == length[i] - 1:                                      #If y < x and length[j] == length[i] - 1, there is a max length increasing subsequence ending at i which passes j.
                    count[i] += count[j]                                                      #So add count[j] to count[i].
            count[i] = max(count[i], 1)                                                       #count[i] should be at lease 1.
        maxLength = max(length)                                                               #Find the max length of increasing subsequence of entire nums.
        return sum(count[i] for i in range(len(nums)) if length[i] == maxLength)              #Sum all the count of such max length of increasing subsequences.
