class DoubleLinkedListNode:                                                                                              #Use a double linked list node to store all keys with given count.

    def __init__(self):
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.max = DoubleLinkedListNode()                                                                                #Initialize the max head.
        self.min = DoubleLinkedListNode()                                                                                #Initialize the min tail.
        self.max.next = self.min                                                                                         #Point the next of head to tail.
        self.min.prev = self.max                                                                                         #Point the prev of tail to head.
        self.mapping = {}                                                                                                #Store each node by its count.
        self.count = Counter()                                                                                           #Count each key.

    def inc(self, key: str) -> None:
        self.count[key] += 1                                                                                             #Increase key count.
        if self.count[key] not in self.mapping:                                                                          #If current count is not in mapping, create a new node for current count.
            self.mapping[self.count[key]] = DoubleLinkedListNode()
            insertBefore = self.min if self.count[key] == 1 else self.mapping[self.count[key] - 1]                       #Insert it before tail if count is 1; otherwise insert before the node of count - 1.
            self.mapping[self.count[key]].next = insertBefore
            self.mapping[self.count[key]].prev = insertBefore.prev
            insertBefore.prev.next = self.mapping[self.count[key]]
            insertBefore.prev = self.mapping[self.count[key]]
        self.mapping[self.count[key]].keys.add(key)                                                                      #Add key to current node.
        if self.count[key] - 1 in self.mapping:                                                                          #If the node of count - 1 exists, remove the key from it.
            self.mapping[self.count[key] - 1].keys.remove(key)
            if not self.mapping[self.count[key] - 1].keys:                                                               #If the node of count - 1 has no keys now, remove it from double linked list and mapping.
                self.mapping[self.count[key] - 1].prev.next = self.mapping[self.count[key] - 1].next
                self.mapping[self.count[key] - 1].next.prev = self.mapping[self.count[key] - 1].prev
                self.mapping.pop(self.count[key] - 1)

    def dec(self, key: str) -> None:
        self.count[key] -= 1                                                                                             #Decrease key count.
        if self.count[key] not in self.mapping and self.count[key] > 0:                                                  #If current count is not in mapping and is greater than 0, create a new node for current count.
            self.mapping[self.count[key]] = DoubleLinkedListNode()
            self.mapping[self.count[key]].prev = self.mapping[self.count[key] + 1]                                       #Insert it after the node of count + 1.
            self.mapping[self.count[key]].next = self.mapping[self.count[key] + 1].next
            self.mapping[self.count[key] + 1].next.prev = self.mapping[self.count[key]]
            self.mapping[self.count[key] + 1].next = self.mapping[self.count[key]]
        if self.count[key] > 0:                                                                                          #If count is greater than 0, add key to current node.
            self.mapping[self.count[key]].keys.add(key)

        self.mapping[self.count[key] + 1].keys.remove(key)                                                               #Remove key from the node of count + 1.
        if not self.mapping[self.count[key] + 1].keys:                                                                   #If the node of count + 1 has no keys now, remove it from double linked list and mapping.
            self.mapping[self.count[key] + 1].prev.next = self.mapping[self.count[key] + 1].next
            self.mapping[self.count[key] + 1].next.prev = self.mapping[self.count[key] + 1].prev
            self.mapping.pop(self.count[key] + 1)

    def getMaxKey(self) -> str:
        if not self.max.next.keys:                                                                                       #If the next of max head has no keys, return empty string.
            return ""
        result = self.max.next.keys.pop()                                                                                #Popping one key from the next of max head as result.
        self.max.next.keys.add(result)                                                                                   #Add result back.
        return result                                                                                                    #Return result.

    def getMinKey(self) -> str:
        if not self.min.prev.keys:                                                                                       #If the prev of min tail has no keys, return empty string.
            return ""
        result = self.min.prev.keys.pop()                                                                                #Popping one key from the prev of min tail as result.
        self.min.prev.keys.add(result)                                                                                   #Add result back.
        return result                                                                                                    #Return result.

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
