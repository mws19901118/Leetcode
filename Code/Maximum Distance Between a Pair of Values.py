class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0                                  #Initialzie the indexes to traverse nums1 and nums2.
        result = 0
        while i < len(nums1) and j < len(nums2):     #Traverse while both i and j is not reaching the end.
            if nums1[i] <= nums2[j]:                 #If nums[i] <= nums2[j], update result if necessary then move forward j.
                result = max(result, j - i)
                j += 1
            else:                                    #Otherwise move forward i and set j to at least i.
                i += 1
                j = max(j, i)
        return result
