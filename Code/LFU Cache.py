class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity                                                            #Store capacity.
        self.count = Counter()                                                              #Store count of each key.
        self.itemByCount = defaultdict(OrderedDict)                                         #Store key value pair in OrderedDict by count.
        self.minCount = 0                                                                   #Track the minimum count.

    def get(self, key: int) -> int:
        if key not in self.count:                                                           #If key is not in count, return -1.
            return -1
        result = self.itemByCount[self.count[key]][key]                                     #First find key count then get the value by key in corresponding OrderedDict.
        self.increaseCount(key)                                                             #Process increasing key count. 
        return result                                                                       #Return result.

    def put(self, key: int, value: int) -> None:
        if key not in self.count:                                                           #If key is not in count, initialize the count to be 0.
            self.count[key] = 0
        self.itemByCount[self.count[key]][key] = value                                      #First find key count then update the value by key in corresponding OrderedDict.
        self.increaseCount(key)                                                             #Process increasing key count. 

    def increaseCount(self, key: int) -> None:
        if len(self.count) > self.capacity:                                                 #If length of count is greater than capacity, we need to evict the least frequent key.
            keyToPop = self.itemByCount[self.minCount].popitem(last = False)[0]             #Pop the first inserted key from the OrderDict of min count.
            keyToPopCount = self.count[keyToPop]                                            #Pop key from count.
            self.count.pop(keyToPop)
            if not len(self.itemByCount[self.minCount]):                                    #If now the OrderDict of min count is empty, pop it from items count.
                self.itemByCount.pop(self.minCount)                                         #No need to update min count now as it is during insertion and min count will be update later to the new insertion.

        value = self.itemByCount[self.count[key]].pop(key)                                  #Pop key value value from OrderDict of key count.
        if not len(self.itemByCount[self.count[key]]):                                      #If this OrderDict is empty, pop it from items count.
            self.itemByCount.pop(self.count[key])
            if self.count[key] == self.minCount:                                            #If current count is min count, increase min count, because current count is about to be increase so there is guarenteed a key value pair at min count plus 1.
                self.minCount += 1
        self.count[key] += 1                                                                #Increase key count.
        self.itemByCount[self.count[key]][key] = value                                      #Set the key value in OrderDict of new count.
        self.minCount = min(self.minCount, self.count[key])                                 #Update min count.


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
