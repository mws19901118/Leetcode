class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()                                                                             #Sort meetings in asending order by start time then by end time.
        rooms = [i for i in range(n)]                                                               #Store rooms in a min heap.
        heapq.heapify(rooms)
        meetingsInProgress = []                                                                     #Store the meetingsInProgress(a tuple of end time and room) in a min heap.
        count = Counter()                                                                           #Count the usage of each room.
        for x, y in meetings:                                                                       #Traverse meetings.
            actualStartTime = x                                                                     #Set the actual meeting start time to x.
            while meetingsInProgress and meetingsInProgress[0][0] <= x:                             #While there are meetings in progress and its end time is not greater than x, pop meetingsInProgress.
                endTime, room = heapq.heappop(meetingsInProgress)
                heapq.heappush(rooms, room)                                                         #Free the room when meeting ends and push it back to rooms.
            if not rooms:                                                                           #If still no room, wait until the first meeting ends.
                endTime, room = heapq.heappop(meetingsInProgress)
                actualStartTime = endTime                                                           #Update actual meeting start time to the end time of previous meeting.
                heapq.heappush(rooms, room)                                                         #Free the room when meeting ends and push it back to rooms.
            room = heapq.heappop(rooms)                                                             #Pop the available room with lowest room number.
            heapq.heappush(meetingsInProgress, (actualStartTime + y - x, room))                     #Push current meeting to meetingsInProgress with actual end time and room.
            count[room] += 1                                                                        #Increase the usage of current room.
        maxCount = max(count.values())                                                              #Find the max usage of rooms.
        for i in range(n):                                                                          #Traverse rooms, when current room's usage is the max usage, return current room.
            if count[i] == maxCount:
                return i
