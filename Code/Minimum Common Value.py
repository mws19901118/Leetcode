class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1).intersection(set(nums2))        #Get the intersection of nums1 and nums2.
        return -1 if not intersection else min(intersection)      #Return -1 if no intersection; otherwise, return min(intersection).
