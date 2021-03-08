class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.modulo = 1000                                                                                                      #Use a modulo to hash keys in to 1000 lists.
        self.lists = [[] for _ in range(1000)]                                                                                  #Initialize the 1000 lists.

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = key % 1000                                                                                                          #Get the hash of key.
        for i, x in enumerate(self.lists[k]):                                                                                   #Traverse the corresponding list.
            if x[0] == key:                                                                                                     #If key exists, override its value and return.
                self.lists[k][i] = (key, value)
                return
        self.lists[k].append((key, value))                                                                                      #If key does not exist, append the key value pair to list.

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = key % 1000                                                                                                          #Get the hash of key.
        for x in self.lists[k]:                                                                                                 #Traverse the corresponding list.
            if x[0] == key:                                                                                                     #If key exists, return its value.
                return x[1]
        return -1                                                                                                               #If key does not exist, return -1.

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = key % 1000                                                                                                          #Get the hash of key.
        index = -1
        for i, x in enumerate(self.lists[k]):                                                                                   #Traverse the corresponding list to find the index of key.
            if x[0] == key:
                index = i
                break
        if index != -1:                                                                                                         #If key exists, swap it with the last element in the list and pop list.
            self.lists[k][-1], self.lists[k][index] = self.lists[k][index], self.lists[k][-1]
            self.lists[k].pop()

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
