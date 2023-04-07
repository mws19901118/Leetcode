class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)                               #Convert nums1 and nums2 to set.
        return [list(set1 - set2), list(set2 - set1)]                     #Return set1 - set2 and set2 - set1.
