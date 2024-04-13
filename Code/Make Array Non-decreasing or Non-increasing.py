class Solution:
    def convertArray(self, nums: List[int]) -> int:
        non_increasing = 0                                            #Initialize cost of making array non-increasing.
        heap = []                                                     #Use a min heap to store all numbers visited.
        for x in nums:                                                #Traverse nums.
            if heap and x > heap[0]:                                  #If current number is larger than the top of head, we have to do operations.
                non_increasing += x - heapq.heappop(heap)             #Pop the heap, let's say it is y, then make x - y opeartions. Then the adjusted value of x, y count be any number between [y, x].
                heapq.heappush(heap, x)                               #After adjust y to x, push x back to heap.
            heapq.heappush(heap, x)                                   #Push x to heap.
                                                                      #Suppose there is an incoming number z(after adjustment). If z is smaller than y, x and y stay (y, y); if z is between y and x, x and y can be both z, z.
        non_decresing = 0                                             #Do the same thing to calulate the cost of making arrary non-decreasing.
        heap = []
        for n in nums:
            if heap and -x > heap[0]:
                non_decresing += -x - heapq.heappop(heap)
                heapq.heappush(heap, -x)
            heapq.heappush(heap, -x)

        return min(non_increasing, non_decresing)                     #Return the lesser cost.
