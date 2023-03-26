class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []                                                                   #Initialize a min heap.
        minV, maxV = float('inf'), float('-inf')                                    #Initialize the min value and max value of heap.
        for i, x in enumerate(nums):                                                #Push the first element of each list to heap and update minV and maxV.
            heapq.heappush(heap, (x[0], i, 0))
            minV = min(minV, x[0])
            maxV = max(maxV, x[0])
        interval = [minV, maxV]                                                     #[minV, maxV] becomes the first candidate.

        while heap:                                                                 #While heap is not empty, traverse.
            value, row, column = heapq.heappop(heap)                                #Pop top of the heap.
            column += 1                                                             #Move to next element of the corresponding list.
            if column == len(nums[row]):                                            #If it is the end, break.
                break
            maxV = max(maxV, nums[row][column])                                     #Update maxV.
            heapq.heappush(heap, (nums[row][column], row, column))                  #Push the element to heap.
            minV = heap[0][0]                                                       #Update minV.
            if interval[1] - interval[0] > maxV - minV:                             #Update interval if [minV, maxV] is shorter.
                interval = [minV, maxV]
        
        return interval                                                             #Return interval.
