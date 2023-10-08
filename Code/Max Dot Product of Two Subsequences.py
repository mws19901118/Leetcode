class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache                                                                                                      #Cache result.
        def dp(i: int, j: int) -> int:                                                                              #Use DP to find the max dot product of 2 subsequences of nums1[:i] and nums2[:j].
            if not i or not j:                                                                                      #If either i or j is 0, return float('-inf') as it is invalid.
                return float('-inf')
            return max(dp(i - 1, j), dp(i, j - 1), nums1[i - 1] * nums2[j - 1] + max(0, dp(i - 1, j - 1)))          #Return the max of dp(i - 1, j)(not using nums1[i - 1]), dp(i, j - 1)(not using nums2[j - 1) and nums1[i - 1] * nums2[j - 1] + max(0, dp(i - 1, j - 1))(using nums1[i - 1] and nums2[j - 1] as a pair).
        return dp(len(nums1), len(nums2))                                                                           #Return dp(len(nums1), len(nums2)).
