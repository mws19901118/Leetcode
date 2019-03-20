# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []                                                             #Use stack to store nested integers.
        for x in reversed(nestedList):                                              #Push all the initial nested integers to stack in reverse order.
            self.stack.append(x)

    def next(self):
        """
        :rtype: int
        """
       return self.stack.pop().getInteger()                                         #Pop stack and return its value.

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack and not self.stack[-1].isInteger():                        #While the stack is not empty and the top of stack is list.
            for x in reversed(self.stack.pop().getList()):                          #Pop stack and get its list.
                self.stack.append(x)                                                #Push nested integers in list to stack in reverse order.
                
        return self.stack                                                           #Return if the stack is empty

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
