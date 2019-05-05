import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []                                           #Use an array to store the values.
        self.map = {}                                             #Use a map to store the index in array of each element.

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:                                       #If val is already in map, return false.
            return False
        self.array.append(val)                                    #Append val to array.
        self.map[val] = len(self.array) - 1                       #Add the index of val to map.
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:                                   #If val is not in map, return false.
            return False
        self.map[self.array[-1]] = self.map[val]                  #Update the index of the last element to be index of val.
        self.array[self.map[val]] = self.array[-1]                #Also move the last element to the index of val.
        self.array.pop()                                          #Remove the last element.
        del self.map[val]                                         #Delete the index of val from map.
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.array[random.randint(0, len(self.array) - 1)] #Return a random element in array.

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
