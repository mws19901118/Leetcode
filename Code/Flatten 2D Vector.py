class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d                                    #Store the 2d vector.
        self.count = 0                                        #Count the total number of elements.
        self.current = 0                                      #Record the number of order of current element.
        self.row = 0                                          #Record the index of current row.
        self.column = 0                                       #Record the index of current column.
        for l in self.vec2d:                                  #Calculate the total number of elements.
            self.count += len(l)

    def next(self):
        """
        :rtype: int
        """
        while self.column == len(self.vec2d[self.row]):       #If current element reaches the end of current row, go to the next row.
            self.row += 1
            self.column = 0
        temp = self.vec2d[self.row][self.column]              #Get the value.
        self.column += 1                                      #Update current index of column.
        self.current += 1                                     #Update current number of order.
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current < self.count                      #If self.current is smaller than self.count, there is next element; otherwise there ain't.

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
