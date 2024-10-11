class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sortedTimestamp = []                              #Initialize sorted timestamps.
        for i, (x, y) in enumerate(times):                #Traverse times.
            sortedTimestamp.append((x, i + 1))            #Append arrival time and i + 1 to sortedTimestamp.
            sortedTimestamp.append((y, -i - 1))           #Append leaving time and -(i + 1) to sortedTimestamp.
        sortedTimestamp.sort()                            #Sort sortedTimestamp.
        heap = []                                         #Use heap to store used seats.
        unused = 0                                        #Store the smallest unused seat.
        seats = {}                                        #Store seat for each friend.
        for x, i in sortedTimestamp:                      #Traverse sortedTimestamp.
            if i > 0:                                     #If i > 0, it is arrival.
                if not heap:                              #If heap is empty, assign usused to current friend and increase unused.
                    seats[i] = unused
                    unused += 1
                else:                                     #Otherwise, pop the smallest seat from heap and assign it to current friend.
                    seats[i] = heapq.heappop(heap)
                if i == targetFriend + 1:                 #If current friend is target friend, return its seat.
                    return seats[i]
            else:                                         #If i < 0, it is leaving.
                heapq.heappush(heap, seats.pop(-i))       #Pop the seat of current friend and push it to heap.
