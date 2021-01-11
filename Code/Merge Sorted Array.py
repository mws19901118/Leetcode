class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:                    #Traverse nums1 and nums2 from back to front until reaches the start of either list.
            if nums1[i] <= nums2[j]:                #if nums1[i] <= nums2[j], put nums2[j] to nums1[i + j + 1] and decrease j by 1.
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:                                   #Otherwise put nums1[i] to nums1[i + j + 1] and decrease i by 1.
                nums1[i + j + 1] = nums1[i]
                i -= 1
        while i >= 0:                               #Put remaining of nums1 in proper positions.
            nums1[i + j + 1] = nums1[i]
            i -= 1
        while j >= 0:                               #Put remaining of nums2 in proper positions.
            nums1[i + j + 1] = nums2[j]
            j -= 1
