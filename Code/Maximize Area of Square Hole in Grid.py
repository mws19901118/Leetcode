class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()                                                              #Sort hBars.
        vBars.sort()                                                              #Sort vBars.
        def longestConsecutive(bars: List[int]):                                  #Find the longest consecutively increasing integers subarray. 
            i, length = 0, 0
            while i < len(bars):
                j = i + 1
                while j < len(bars) and bars[j] == bars[j - 1] + 1:
                    j += 1
                length = max(length, j - i)
                i = j
            return length
        length = min(longestConsecutive(hBars), longestConsecutive(vBars))        #Find the smaller value of the longest consecutively increasing integers subarray of hBars and vBars.
        return (length + 1) ** 2                                                  #Since removing x bars freeing up x + 1 cells, return (length + 1) ** 2.
