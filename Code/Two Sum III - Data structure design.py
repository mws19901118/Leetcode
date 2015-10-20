class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dict = {}                                                              #Use dict to store data. Key is number and value is count.

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.dict:
            self.dict[number] = 1
        else:
            self.dict[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.dict:
            if i * 2 == value:
                if self.dict[i] > 1:
                    return True
            else:
                if value - i in self.dict:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
