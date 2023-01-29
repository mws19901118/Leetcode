class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity                                                                                                #Store capacity.
        self.key_to_frequency = collections.defaultdict(int)                                                                    #Store the frequency of each key.
        self.frequency_to_key_value = collections.defaultdict(OrderedDict)                                                      #Store the key value pair by frequency in an ordered dict.
        self.min_frequency = 0                                                                                                  #Maintain the min frequency.

    def update_frequency(self, key: int, value: int = None) -> int:
        f = self.key_to_frequency[key]                                                                                          #Get the frequency of key.
        v = self.frequency_to_key_value[f].pop(key)                                                                             #Remove the key from current frequency ordered dict.
        if value:                                                                                                               #Update to new value if any.
            v = value

        self.frequency_to_key_value[f + 1][key] = v                                                                             #Add the key to current frequency plust 1.
        self.key_to_frequency[key] += 1                                                                                         #Update the frequency of key.
        if self.min_frequency == f and not self.frequency_to_key_value[f]:                                                      #Increase min frequency if no keys are with min frequency.
            self.min_frequency += 1

        return v                                                                                                                #Return value.

    def get(self, key: int) -> int:
        if key not in self.key_to_frequency:                                                                                    #If key is not found, return -1.
            return -1

        return self.update_frequency(key)                                                                                       #Update the frequency of key.

    def put(self, key: int, value: int) -> None:
        if not self.capacity:                                                                                                   #If capacity is 0, cannot put anything.
            return

        if key in self.key_to_frequency:                                                                                        #If key is in cache, updatet the value and frequency of key.
            self.update_frequency(key, value)
        else:
            if len(self.key_to_frequency) == self.capacity:                                                                     #If cache is full, pop the least frequently used key with min frequency and delete it.
                self.key_to_frequency.pop(self.frequency_to_key_value[self.min_frequency].popitem(last = False)[0])

            self.min_frequency = 1                                                                                              #Add new key value pair with frequency 1, also set min frequency to 1.
            self.key_to_frequency[key] = 1
            self.frequency_to_key_value[1][key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
