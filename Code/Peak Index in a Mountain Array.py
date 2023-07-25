class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1                            #Initialize start and end.
        while start <= end:                                     #Binary search.
            mid = (start + end) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:          #If mid is peak, return mid.
                return mid
            elif arr[mid - 1] > arr[mid]:                       #If mid is on downhill, binary search in the 1st half.
                end = mid
            else:                                               #If mid is on uphill, binary search in the 2nd half.
                start = mid
