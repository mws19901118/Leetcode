# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]                                               #Use stack to store nested integers. Push all the initial nested integers to stack in reverse order.
    
    def next(self) -> int:
        return self.stack.pop().getInteger()                                        #Pop stack and return its value.
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():                        #While the stack is not empty and the top of stack is list.
            top = self.stack.pop().getList()                                        #Pop stack and get its list.
            self.stack.extend(top[::-1])                                            #Push nested integers in list to stack in reverse order.

        return self.stack
