class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        end = 1                                                             #Initialize a sliding window [0, 1].
        while reader.get(end) != 2147483647 and reader.get(end) < target:   #If the value at end is not 2147483647 or is smaller than target, target is not in current window.
            end = end << 1                                                  #Slide window to right and double the size.
        start = end >> 1
        while start <= end:                                                 #Binary search target in sliding window.
            mid = (start + end) >> 1
            temp = reader.get(mid)
            if temp == target:
                return mid
            elif temp == 2147483647 or temp > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
