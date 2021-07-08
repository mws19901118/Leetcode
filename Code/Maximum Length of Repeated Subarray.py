class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        dp = [0] * len(nums2)                                                         #Initialize dp array with the length of nums2's length, indicating the max repeated length of subarray ending at each number of nums2.
        for i in range(len(nums1)):                                                   #Traverse nums1.
            prev = 0                                                                  #Initialize prev to 0, which means the dp[j - 1] from i - 1 iteration.
            for j in range(len(nums2)):                                               #Traverse nums2.
                prev, dp[j] = dp[j], prev + 1 if nums1[i] == nums2[j] else 0          #If nums1[i] == nums2[j], dp[j] = prev + 1; otherwise 0. Also update prev to old dp[j].
                result = max(result, dp[j])                                           #Update result if necessary.
        return result
