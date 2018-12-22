class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()              #Use deque.
        self.limit = 3000                             #Set limit.
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)                          #Add t to queue.
        while self.queue[0] + self.limit < t:         #Popleft all the oboselete calls.
                self.queue.popleft()
        return len(self.queue)                        #Return length.
    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
