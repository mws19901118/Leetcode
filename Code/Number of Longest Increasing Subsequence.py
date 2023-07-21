class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(0, 0)] * len(nums)                                    #Initialize dp list.
        maxLength = 0                                                #Initialize max length.
        for i, x in enumerate(nums):                                 #Traverse nums.
            length, count = 1, 1                                     #Initialize the max length ending at current number and its count.
            for j, y in enumerate(nums[:i]):                         #Traverse nums[:i].
                if y < x:                                            #If y < x, we find at least one new increasing subsequence.
                    if dp[j][0] + 1 > length:                        #If dp[j][0] + 1 > length, the new increaseing subsequence is longer than current max length.
                        length, count = dp[j][0] + 1, dp[j][1]       #Update length and count.
                    elif dp[j][0] + 1 == length:                     #If d[j][0] + 1 == length, directly add dp[j][1] to count.
                        count += dp[j][1]
            maxLength = max(length, maxLength)                       #Update maxLength.
            dp[i] = (length, count)                                  #Set dp[i[ to (length, count).
        return sum(c for l, c in dp if l == maxLength)               #Return the sum of count of subsequences whose length is maxLength.
