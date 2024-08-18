class Twitter:

    def __init__(self):
        self.timeId = 0                                                                                                                                            #Have a time id for each twitter, starting from 0 and decrease 1 each time(to be used as the order in max heap).
        self.feedLimit = 10
        self.tweetMap = defaultdict(list)                                                                                                                          #Store tweets for each user.
        self.followMap = defaultdict(set)                                                                                                                          #Store followers for each user.

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timeId, tweetId))                                                                                                       #Append timeId and tweetId to self.tweetMap[userId].
        self.timeId -= 1                                                                                                                                           #Decrease timeId.

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []                                                                                                                                                  #Initialize max heap.
        for followeeId in (self.followMap[userId] | set([userId])):                                                                                                #Traverse followees of userId as well as userId it self.
            if self.tweetMap[followeeId]:                                                                                                                          #If the followeeId has tweet, push its last tweet timeId, tweetId, follweeId and the index of last tweet in self.tweetMap[followeeId] to max heap.
                heapq.heappush(heap, (self.tweetMap[followeeId][-1][0], self.tweetMap[followeeId][-1][1], followeeId, len(self.tweetMap[followeeId]) - 1))
        result = []
        while heap and len(result) < self.feedLimit:                                                                                                               #Iterate while heap is not empty and result hasn't reach the feed limit.
            timeId, tweetId, followeeId, index = heapq.heappop(heap)                                                                                               #Pop max heap.
            result.append(tweetId)                                                                                                                                 #Append tweetId to result.
            if index > 0:                                                                                                                                          #If index > 0, there are more tweets for the followeeId.
                index -= 1                                                                                                                                         #Decrese index to move backwards to get the latest unvisited tweet of followeeId.
                heapq.heappush(heap, (self.tweetMap[followeeId][index][0], self.tweetMap[followeeId][index][1], followeeId, index))                                #Push the current timeId, tweetId, followeeId and index to max heap.
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)                                                                                                                 #Add followeeId to self.followMap[followerId].

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)                                                                                                             #Discard followeeId from self.followMap[followerId].


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
