class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        minHeights = []                                               #Track min highets of last obstacles of each length.
        result = [0] * len(obstacles)                                 #Initialize result.
        for i, x in enumerate(obstacles):                             #Traverse obstacles.
            index = bisect_right(minHeights, x)                       #Binary serach the rightmost index to insert x in minHeights.
            if index == len(minHeights):                              #If it's the end of minHeights, append x to minHeights.
                minHeights.append(x)
            else:                                                     #Otherwise, update minHeights[index] if x is smaller than current minHieghts[index].
                minHeights[index] = min(minHeights[index], x)
            result[i] = index + 1                                     #Set result[i] to index + 1, because there is a valid obstacle course whose length is index and its last obstacle is not taller than x.
        return result
