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
