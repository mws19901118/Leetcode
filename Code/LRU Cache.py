#DoubleLinkedList + Dict Solution:
class DoubleLinkedList(object):                                                     #Construct the node of double linked list.
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}                                                              #Store the double linked list node corresponding to its key.
        self.head = DoubleLinkedList('head', -1)                                    #It's the dummy head node.
        self.tail = DoubleLinkedList('tail', -1)                                    #It's the Dummy tail node.
        self.head.next = self.tail                                                  #Initialize the double linked list.
        self.tail.prev = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dict:                                                    #If current key is not in the cache, return -1.
            return -1
        curr = self.dict[key]                                                       #Find the corresponding double linked list node according to its key.
        curr.next.prev = curr.prev                                                  #Unlink it with its previous node and next node.
        curr.prev.next = curr.next
        curr.next = self.head.next                                                  #Insert it behind the head node.
        self.head.next.prev = curr
        curr.prev = self.head
        self.head.next = curr
        return curr.val                                                             #Return its value.

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:                                                        #If current key is in the cache, find the corresponding linked list node.
            curr = self.dict[key]
            curr.next.prev = curr.prev                                              #Unlink it with its previous node and next node.
            curr.prev.next = curr.next
            curr.next = self.head.next                                              #Insert it behind the head node.
            self.head.next.prev = curr
            curr.prev = self.head
            self.head.next = curr
            curr.val = value                                                        #Update the its value.
        else:                                                                       #Otherwise, construct a new double linked list node with current key and value.
            curr = DoubleLinkedList(key, value)
            self.dict[key] = curr                                                   #Add it to the dict.
            curr.next = self.head.next                                              #Insert it behind the head node.
            self.head.next.prev = curr
            curr.prev = self.head
            self.head.next = curr
            if len(self.dict) > self.capacity:                                      #If current count of nodes exceeds the capacity.
                lru = self.tail.prev                                                #Remove the node before the tail node form the double linked list and the dict.
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
                del self.dict[lru.key]

#OrderedDict Solution:
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        LRUCache.Dict = collections.OrderedDict()
        LRUCache.capacity = capacity
        LRUCache.numItems = 0

    # @return an integer
    def get(self, key):
        try:
            value = LRUCache.Dict[key]
            del LRUCache.Dict[key]                            #delete old value, add new one
            LRUCache.Dict[key] = value
            return value
        except:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del LRUCache.Dict[key]                            #delete old value, add new one
            LRUCache.Dict[key] = value
            return
        except:
            if LRUCache.numItems == LRUCache.capacity:        
                LRUCache.Dict.popitem(last = False)           #use 'last=False' delete LRU item
                LRUCache.numItems -= 1
            LRUCache.Dict[key] = value                        #add new item
            LRUCache.numItems += 1
        return
