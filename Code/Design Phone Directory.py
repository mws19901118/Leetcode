import random
class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.m = maxNumbers
        self.s = set([i for i in range(maxNumbers)])                              #Use set to store the remaining valid numbers.
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.s) == 0:                                                      #If the length of set is 0, return -1.
            return -1
        v = random.sample(self.s, 1)[0]                                           #Sample a value from s.
        self.s.remove(v)                                                          #Remove the sample from set.
        return v                                                                  #Return the value.
        
    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.s                                                   #Return if numebr is in s.

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        self.s.add(number)                                                        #Add number to s.


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
