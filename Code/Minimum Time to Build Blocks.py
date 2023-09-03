class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:        
        heapq.heapify(blocks)                              #Store blocks building time in a min heap.
        while len(blocks) > 1:                             #Iterate while there are more than one blocks in heap.
            x = heapq.heappop(blocks)                      #If we have 2 blocks x and y (x < y) but only one worker, we have to split the worker first then assign them to the 2 blocks.          
            y = heapq.heappop(blocks)                      #Thus, it becomes a virtual block whose building time is split + y.
            heapq.heappush(blocks, split + y)              #So, we keep iterating by popping the 2 blocks with shortest building time, forming a new virtual block then pushing back to min heap. Since we postpone shorter block as much as possible and pick up larger blocks so the overall time is optimal.
        return heapq.heappop(blocks)                       #Return the final building time in heap.
