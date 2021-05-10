class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []                                                 #Use a min heap to maintain the largest ladders gap. Because we want to use ladder for the heigher gap as many as possible
        for i in range(len(heights) - 1):                         #Traverse heights.
            if heights[i] >= heights[i + 1]:                      #If current building is higher than or equal to next building, continue.
                continue
            heapq.heappush(heap, heights[i + 1] - heights[i])     #Push the gap to heap.
            if len(heap) > ladders:                               #If the length of heap is larger than ladders, pop heap and subtract it from bricks.
                bricks -= heapq.heappop(heap)
            if bricks < 0:                                        #If bricks is smaller than 0, we cannot go further, so return i.
                return i
        return len(heights) - 1                                   #Return len(heights) - 1 if we can reach the last building.
