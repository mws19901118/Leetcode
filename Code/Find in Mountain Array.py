# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()                                                                                                      #Get the length of arr.

        def findPeakIndex():                                                                                                                #Binary search for index of peak.
            start, end = 0, length - 1
            peakIndex = -1
            while start <= end:
                mid = (start + end) // 2
                curr = mountain_arr.get(mid)
                if (mid - 1 >= 0 and curr > mountain_arr.get(mid - 1)) and (mid + 1 < length and curr > mountain_arr.get(mid + 1)):
                    peakIndex = mid
                    break
                elif mid - 1 < 0 or (mid + 1 < length and curr < mountain_arr.get(mid + 1)):
                    start = mid + 1
                else:
                    end = mid - 1
            return peakIndex

        def findInUphill():                                                                                                                #Binary search in uphill.
            start, end = 0, peakIndex
            index = -1
            while start <= end:
                mid = (start + end) // 2
                curr = mountain_arr.get(mid)
                if curr == target:
                    index = mid
                    break
                elif curr < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return index

        def findInDownhill():                                                                                                              #Binary search in downhill.
            start, end = peakIndex, length - 1
            index = -1
            while start <= end:
                mid = (start + end) // 2
                curr = mountain_arr.get(mid)
                if curr == target:
                    index = mid
                    break
                elif curr > target:
                    start = mid + 1
                else:
                    end = mid - 1
            return index
        
        peakIndex = findPeakIndex()                                                                                                       #Find the index of peak first.
        index = findInUphill()                                                                                                            #Find target in uphill.
        return index if index != -1 else findInDownhill()                                                                                 #If target found, return index; otherwise return the result of finding target in downhill.
