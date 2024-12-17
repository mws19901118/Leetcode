class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(x), c) for x, c in Counter(s).items()]      #Count each character and put its ascii and count in max heap.
        heapq.heapify(heap)
        hold = None                                               #Hold the current lexicographically largest character which is just added to result and cannot be pushed back to max heap.
        result = []
        while heap:                                               #Iterate while heap is not empty.
            x, c = heapq.heappop(heap)                            #Pop the heap top.
            if result and result[-1][0] == x:                     #If result is not empty and last character in result is same as current character, we cannot add more to result, so stop.
                break
            segmentCount = 1 if hold else min(c, repeatLimit)     #The character count in current segment is 1 if there is hold, which is a lexicographically larger character; otherwise is the min of current character count and repeatLimit.
            result.append((x, segmentCount))                      #Append current character and the segment count to result.
            if hold:                                              #If there is a hold, push it back to max heap and reset hold to none.
                heapq.heappush(heap, hold)
                hold = None
                if c > segmentCount:                              #If there is current character left, push it and updated count back to max heap.
                    heapq.heappush(heap, (x, c - segmentCount))
            elif c > segmentCount:                                #If there is no hold and there is current character left, set it and updated count to hold.
                hold = x, c - segmentCount
        return "".join([chr(-x) * c for x, c in result])          #Traverse result and convert asaii back to character and repeat its segment count times then join together and return.
