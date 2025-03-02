class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0                                                          #Initialize pointers to traverse nums1 and nums2 respectively.
        result = []                                                          #Initialize result.
        while i < len(nums1) and j < len(nums2):                             #Iterate while both i and j not reaching the end.
            if nums1[i][0] == nums2[j][0]:                                   #If nums1[i] and nums2[i] have same id, append the id with sum of 2 values to result, then move forward i and j.
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:                                  #If nums1[i] has a smaller id, append nums1[i] to result and move forward i.
                result.append(nums1[i])
                i += 1
            else:                                                            #Otherwise, append nums2[j] to result and move forward j.
                result.append(nums2[j])
                j += 1
        if i < len(nums1):                                                   #If i not reaching end, extend the nums1[i:] to result.
            result.extend(nums1[i:])
        else:                                                                #Otherwise, extend nums2[j:] to result.
            result.extend(nums2[j:])
        return result
