class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order, heap = [], []                                                                      #Initialize order and min heap.
        currentTime, index = 1, 0                                                                 #Initialize current time and index.
        tasksWithIndex = sorted((x[0], x[1], i) for i, x in enumerate(tasks))                     #Sort tasks by enqueueTime and preserve the original index. 
        while heap or index < len(tasksWithIndex):                                                #Iterate while heap is not empty or index not reaching the end.
            if heap:                                                                              #If min heap is not empty, pop the task on top of heap.
                processingTime, currentIndex = heapq.heappop(heap)
                currentTime += processingTime                                                     #Process the task and add index to order.
                order.append(currentIndex)
            while index < len(tasksWithIndex) and tasksWithIndex[index][0] <= currentTime:        #Push all the tasks whose enqueueTime is smaller than or equal to current time to min heap.
                heapq.heappush(heap, (tasksWithIndex[index][1], tasksWithIndex[index][2]))
                index += 1
            if not heap and index < len(tasksWithIndex):                                          #If min heap is still empty, CPU is idle, so move to next closest task.
                currentTime = tasksWithIndex[index][0]
        return order                                                                              #Return order.
