# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution:
    def calculate(self, nestedInteger: NestedInteger, depth: int) -> int:
        return depth * nestedInteger.getInteger() if nestedInteger.isInteger() else sum(self.calculate(x, depth + 1) for x in nestedInteger.getList())              #Calculate depth sum for a nested integer with given sum. If it's integer, return the value multuply the depth; otherwise, calculate the depth sum for each nested integer in the list recursively.

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return sum(self.calculate(x, 1) for x in nestedList)                                                                                                        #Return the sum of depth sum for given nested integer list.
