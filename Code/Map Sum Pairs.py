class Trie:                                                                     #Trie implementation.
    def __init__(self):
        self.dict = defaultdict(Trie)                                           #Use default dict to store trie node for next level.
        self.total = 0                                                          #Initialize sum for current level.
        
    def insert(self, key: str, delta: int) -> None:                             #Insert sum delta for given key.
        self.total += delta                                                     #Update total.
        if key:                                                                 #If key is not empty, insert key[1:] as key and delta to the trie node of key[0].
            self.dict[key[0]].insert(key[1:], delta)
    
    def sum(self, prefix: str) -> int:                                          #Return the sum of given prefix.
        if not prefix:                                                          #If prefix is empty, return current total.
            return self.total
        return self.dict[prefix[0]].sum(prefix[1:])                             #Otherwise, return the total from trie node of prefix[1:].
        
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(int)                                            #Initialize a dict for storing the key value pair.
        self.trie = Trie()                                                      #Initialize trie.

    def insert(self, key: str, val: int) -> None:
        delta = val - self.dict[key]                                            #Compute the value delta for key.
        self.dict[key] = val                                                    #Update the value of key in dict.
        self.trie.insert(key, delta)                                            #Insert delta for key in trie.

    def sum(self, prefix: str) -> int:
        return self.trie.sum(prefix)                                            #Return the sum of prefix.


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
