class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, heap = [], []                            #Initialize result and a max heap.
        for x, y in [(a, 'a'), (b, 'b'), (c, 'c')]:      #Traverse a, b, c and push the count and character to heap if count is not 0.
            if x:
                heapq.heappush(heap, (-x, y))
        hold = None                                      #Store the count and character on hold.
        while heap:                                      #Iterate while heap is not empty.
            x, y = heapq.heappop(heap)                   #Pop the top of heap.
            result.append(y)                             #append character to result.
            if hold:                                     #If there is count and character on hold, push it back to heap and result hold.
                heapq.heappush(heap, hold)
                hold = None
            x += 1                                       #Decrease count.
            if not x:                                    #If count is 0 now, continue.
                continue
            if len(result) >= 2 and result[-2] == y:     #If there are already 2 consecutive current characters at the end of result, put current character on hold.
                hold = (x, y)
            else:                                        #Otherwise push the count and character back to heap.
                heapq.heappush(heap, (x, y))
        return "".join(result)                           #Join result and return.
