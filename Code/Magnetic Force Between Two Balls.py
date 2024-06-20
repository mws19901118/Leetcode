class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        @cache                                                                     #Cache result.
        def canDistribute(threshold: int) -> bool:                                 #Check if it is possible to distribute balls with given min distance threshold.
            index, count = 0, 1                                                    #Initialize last ball index and count.
            for i, x in enumerate(position):                                       #Traverse position.
                if x - position[index] >= threshold:                               #If current basket has at least threshold distance with last ball, place ball here and update index.
                    count += 1
                    index = i
            return count >= m                                                      #Return if more than m balls placed.

        position.sort()                                                            #Sort position.
        start, end = 1, max(position)                                              #Min distance is 1 and max distance is the max in position.
        while start <= end:                                                        #Binary search for the max of min distance.
            mid = (start + end) // 2
            if canDistribute(mid) and not canDistribute(mid + 1):
                return mid
            elif not canDistribute(mid):
                end = mid - 1
            else:
                start = mid + 1
