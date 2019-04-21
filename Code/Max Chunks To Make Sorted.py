class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count, m = 0, 0                   #Count chucks and store the max value while traversing.
        for i, x in enumerate(arr):
            m = max(m, x)                 #For each value in arr, update the current max value/
            if m == i:                    #Since array start from 0, whenever the current max equals index of current value, the values from last chunk ends to here forms a new chuck.
                count += 1                #Increase count by 1.
        return count                      #Return count.
