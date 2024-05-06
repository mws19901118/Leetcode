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
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def getDepth(nestedList: List[NestedInteger]) -> int:                                                                    #Get depth for current nested list.
            return 0 if not nestedList else max(1 if x.isInteger() else (getDepth(x.getList()) + 1) for x in nestedList)         #Return 0 if list is empty; otherwise return the max of each individual nested integer: 1 if it is int or the recursive depth plus 1 if it is list.

        def calculateSum(nestedList: List[NestedInteger], weight) -> (int, int):                                                 #Calculate sum with given weight.
            return sum(x.getInteger() * weight if x.isInteger() else calculateSum(x.getList(), weight - 1) for x in nestedList)  #Sum up weighted sum for each individual nested integer: number * weight if it is int or the recursive weighted sum if it is list.
        
        return calculateSum(nestedList, getDepth(nestedList))                                                                    #Get depth as max weight and calculate weighted sum starting from max weight.
