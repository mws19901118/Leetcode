class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)                                              #Calculate sum of nums1 and nums2.
        l1, l2 = sum(not x for x in nums1), sum(not x for x in nums2)                #Count zeros in nums1 and nums2.
        if (s1 + l1 < s2 + l2 and not l1) or (s2 + l2 < s1 + l1 and not l2):         #If after replacement, sum of one array is smaller than sum of the other and smaller array does not have zero, then cannot make 2 arrays equal.
            return -1
        return max(s1 + l1, s2 + l2)                                                 #Return the max of sum after replacement.
