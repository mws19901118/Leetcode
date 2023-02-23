class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        tasks = sorted([(c, p) for c, p in zip(capital, profits)])            #Sort tasks by capital in ascending order.
        heap, index = [], 0                                                   #Initialize a max heap and a pointer to traverse tasks.
        for i in range(k):                                                    #Iterate k times.
            while index < len(tasks) and tasks[index][0] <= w:                #Push the profit of each task whose capital is not greater than w into the max heap.
                heapq.heappush(heap, -tasks[index][1])
                index += 1
            if not heap:                                                      #If heap is empty, no task can be picked up, so jump out of loop.
                break
            p = heapq.heappop(heap)                                           #Pop the heap top.
            w -= p                                                            #Add the profit to w.
        return w                                                              #Return w.
