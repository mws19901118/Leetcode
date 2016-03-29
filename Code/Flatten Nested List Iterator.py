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
        self.currentList = nestedList                                                                                                       #Store current nested list.
        self.currentIndex = 0                                                                                                               #Store current index in current nested list.
        self.stack = []                                                                                                                     #Store the state in the preivous level of DFS.

    def next(self):
        """
        :rtype: int
        """
        temp = self.currentList[self.currentIndex].getInteger()                                                                             #Get current integer.
        self.currentIndex += 1                                                                                                              #Increase current index by 1.
        return temp                                                                                                                         #Return value.
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while not (self.currentIndex == len(self.currentList) and self.stack == []):                                                        #If current index equals the length of current list and stack is empty, we reach the end of nested list.
            while self.currentIndex == len(self.currentList) and self.stack:                                                                #If current index reaches the end of current list, pop stack while it's not empty.
                self.currentList = self.stack[-1][0]
                self.currentIndex = self.stack[-1][1] + 1
                self.stack.pop()
            while self.currentIndex < len(self.currentList) and self.currentList[self.currentIndex].isInteger() is False:                   #If current object is list, push current list and current index to stack and go into the new list.
                self.stack.append((self.currentList, self.currentIndex))
                self.currentList = self.currentList[self.currentIndex].getList()
                self.currentIndex = 0
            if self.currentIndex < len(self.currentList) and self.currentList[self.currentIndex].isInteger() is True:                       #If current object is integer, return true.
                return True
        return False                                                                                                                        #Return false.

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
