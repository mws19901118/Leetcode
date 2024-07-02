class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1) & Counter(nums2)                 #Count nums1 and nums2 and get intersection.
        result = []
        for x in count:                                         #For each number in count, append count[x] times to result.
            result.extend([x] * count[x])
        return result
