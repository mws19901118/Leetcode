class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = 1                                               #Start with index 1, because peak index cannot be on edge.
        end = len(A) - 2                                        #End with index len(A) - 2, because peak index cannot be on edge.
        while start <= end:                                     #Binary search.
            mid = (start + end) / 2
            if A[mid - 1] < A[mid] and A[mid + 1] < A[mid]:     #If mid is peak, return mid.
                return mid
            elif A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:   #If mid is on uphill, binary search in the 2nd half.
                start = mid + 1
            else:                                               #If mid is on downhill, binary search in the 1st half.
                end = mid - 1
