class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()                                                          #Sort events buy starting day in asending order, then by ending day in asending order.
        result, day, index = 0, 0, 0                                           #Initialize result, current day and index to traverse events.
        heap = []                                                              #Store the current visited but not attended event by ending day in a min heap.
        while index < len(events) or heap:                                     #Iterate while index hasn't reached the end or heap is not empty.
            if not heap:                                                       #If heap is empty, move day to the starting day of current event.
                day = events[index][0]
            while index < len(events) and events[index][0] <= day:             #While index hasn't reached the end and the starting day of current event is not greater than current day, push the event to min heap.
                heapq.heappush(heap, (events[index][1], events[index][0]))
                index += 1
            while heap:                                                        #Pop heap while it is not empty.
                y, x = heapq.heappop(heap)
                if y >= day:                                                   #If the ending day of the popped event is not smaller than current day, we can attend the event.
                    day += 1                                                   #Increase day.
                    result += 1                                                #Increase result.
                    break                                                      #Jump out of loop.
        return result
