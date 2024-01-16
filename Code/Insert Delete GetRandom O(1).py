class RandomizedSet:

    def __init__(self):
        self.values = []                                                              #Use a list to store the values.
        self.indexes = {}                                                             #Use a dictionary to store the index of each element in list.

    def insert(self, val: int) -> bool:
        if val in self.indexes:                                                       #If val is already in dictionary, return false.
            return False
        self.values.append(val)                                                       #Append val to list.
        self.indexes[val] = len(self.values) - 1                                      #Add the index of val to dictionary.
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:                                                   #If val is not in dictionary, return false.
            return False
        self.indexes[self.values[-1]] = self.indexes[val]                             #Update the index of the last element to be index of val.
        self.values[self.indexes[val]] = self.values[-1]                              #Also move the last element to the index of val.
        self.indexes.pop(val)                                                         #Delete the index of val from dictionary.
        self.values.pop()                                                             #Pop the last element.
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)                                             #Return a random element in list.
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
