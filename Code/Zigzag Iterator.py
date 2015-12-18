class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = []                                 #Store elements in zigzag order.
        for i in range(min(len(v1), len(v2))):
            self.v.append(v1[i])
            self.v.append(v2[i])
        if len(v1) > len(v2):
            for i in range(len(v2), len(v1)):
                self.v.append(v1[i])
        else:
            for i in range(len(v1), len(v2)):
                self.v.append(v2[i])
        self.current = 0                            #Record the current index.

    def next(self):
        """
        :rtype: int
        """
        self.current += 1                           #Increase current index by 1.
        return self.v[self.current - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.current < len(self.v):              #If current index is smaller than the total number of elements, return true.
            return True
        else:                                       #Otherwise, return false.
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
