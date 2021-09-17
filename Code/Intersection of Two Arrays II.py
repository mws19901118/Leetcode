class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)         #Count nums1 and nums2.
        result = []
        for x in count1:                                        #For each number in count1, find the min value of its count in nums1 and nums2.
            result.extend([x] * min(count1[x], count2[x]))      #Append the number to result for times of min value above.
        return result
