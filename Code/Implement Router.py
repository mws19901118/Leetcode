class Router:

    def __init__(self, memoryLimit: int):
        self.destinationQueues = defaultdict(deque)                                    #Store packet stamps for each destination.
        self.overallQueue = deque()                                                    #Store all current packges in a queue
        self.s = set()                                                                 #Use a set to de-dupe.
        self.limit = memoryLimit                                                       #Store limit.

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source, destination) in self.s:                                 #If the packet is in router, return false.
            return False
        if len(self.s) == self.limit:                                                  #If the router reaches memory limit, drop the earliest packet by faking a forward.
            self.forwardPacket()
        self.destinationQueues[destination].append(timestamp)                          #Add the timestamp the queue of destination.
        self.overallQueue.append((timestamp, source, destination))                     #Add packet to overall queue.
        self.s.add((timestamp, source, destination))                                   #Add packet to set.
        return True                                                                    #Return true.

    def forwardPacket(self) -> List[int]:
        if not self.overallQueue:                                                      #If no package in overall queue, return empty list.
            return []
        t, s, d = self.overallQueue.popleft()                                          #Popleft overall queue to get the earliest packet.
        self.s.remove((t, s, d))                                                       #Remove it from set.
        self.destinationQueues[d].popleft()                                            #Popleft destination queue, because it is guarenteed to be the earlist in destination queue. 
        return [s, d, t]                                                               #Return packet.

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect_left(self.destinationQueues[destination], startTime)             #Find the left most index of start time in destination queue, inclusive
        right = bisect_left(self.destinationQueues[destination], endTime + 1)          #Find the left most index of start time in destination queue, not inclusive.
        return right - left                                                            #Return right - left.


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
