class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)                                                                                  #Count each character in s.
        heap = []                                                                                             #Initialize max heap.
        result = ""                                                                                           #Initialize result.
        for k, v in counter.items():                                                                          #Push all character and its count in max heap order by count.
            heapq.heappush(heap, (-v, k))
        while len(heap) > 1:                                                                                  #Iterate if there is are more than 1 distinct characters in heap.
            countX, x = heapq.heappop(heap)                                                                   #Pop the 2 characters with largest count.
            countY, y = heapq.heappop(heap)
            result += x + y                                                                                   #Append x and y to result.
            if countX + 1 < 0:                                                                                #If there are more x, push x and its updated count back to max heap.
                heapq.heappush(heap, (countX + 1, x))
            if countY + 1 < 0:                                                                                #If there are more y, push y and its updated count back to max heap.
                heapq.heappush(heap, (countY + 1, y))
        return "" if len(heap) == 1 and -heap[0][0] > 1 else result + (heap[0][1] if heap else "")            #If there is a final character left with more than 1 count, return empty string as we cannot reorganize s successfully.
                                                                                                              #Otherwise, append final character left if it has exact one count then return result.
