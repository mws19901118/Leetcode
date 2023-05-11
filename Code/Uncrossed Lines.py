class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for j in range(len(nums2) + 1)] for i in range(len(nums1) + 1)]                                            #dp[i + 1][j + 1] stores the max uncrossed lines between A[:i + 1] and B[:j + 1]
        for i, j in product(range(len(nums1)), range(len(nums2))):                                                          #Traverse nums1 and nums2.
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]) if nums1[i] != nums2[j] else dp[i][j] + 1                    #If nums1[i] == nums2[j], we can draw a line between nums1[i] and nums2[j] so dp[i + 1][j + 1] = dp[i][j] + 1; otherwise, dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]).
        return dp[len(nums1)][len(nums2)]                                                                                   #Return dp[len(nums1)][len(nums2)] as the final result.
