class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        sortedDiff = sorted([x - y for x, y in zip(nums1, nums2)])      #nums1[i] + nums1[j] > nums2[i] + nums2[j] => (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0. It is essentially the unique (i, j) pairs in diff, nums1[x] - nums2[x] that diff[i] + diff[j] > 0. So we calculate diff and sort it.
        result, left, right = 0, 0, len(sortedDiff) - 1                 #Initialize result and 2 pointers pointing to beginning and end.
        while left < right:                                             #Iterate while left < right.
            if sortedDiff[left] + sortedDiff[right] > 0:                #For current right pointer, all numbers in sortedDiff[left:right] makes a valid pair with right, numbers in sortedDiff[:left] is not valied and numbers in sortedDiff[right + 1:] are already counted.
                result += right - left                                  #So add right - left to result and move right backwards.
                right -= 1
            else:                                                       #Otherwise, move left forward.
                left += 1
        return result
