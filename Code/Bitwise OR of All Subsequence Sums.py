class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        result, prefuxSum = 0, 0              #https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/solutions/2912829/java-o-n-time-o-1-space-solution-with-proof/?envType=weekly-question&envId=2024-04-29
        for x in nums:
            prefuxSum += x
            result |= x | prefuxSum
        return result
