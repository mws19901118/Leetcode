class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = defaultdict(int)
        for a, b in product(nums1, nums2):                                          #Count the sum of a + b for each a in nums1 and b in nums2.
            count[a + b] += 1
        return sum(countAB[-(c + d)] for c, d in product(nums3, nums4))             #Return the sum of -(c + d) in count for each c in nums3 and d in nums4.
