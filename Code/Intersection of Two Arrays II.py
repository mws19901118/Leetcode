from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = Counter(nums1)                           #Count each number in nums1.
        count2 = Counter(nums2)                           #Count each number in nums2.
        result = []
        for x in count1:                                  #For each number in count1, find the min value of its count in nums1 and nums2.
            for i in range(min(count1[x], count2[x])):
                result.append(x)                          #Append the number to result for times of min value above.
        return result
