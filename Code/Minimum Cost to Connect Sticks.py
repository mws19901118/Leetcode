class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)                                                                 #Heapify sticks.
        count = 0
        while len(sticks) > 1:                                                                #Iterate while there are more than one sticks.
            newStick = heapq.heappop(sticks) + heapq.heappop(sticks)                          #Always connect the shortest 2 sticks now to minimize the effort, because the early a stick is picked, it will contribute more towards the final cost.  
            heapq.heappush(sticks, newStick)                                                  #Push new stick back to heap.
            count += newStick                                                                 #Increase count of effort.
        return count
