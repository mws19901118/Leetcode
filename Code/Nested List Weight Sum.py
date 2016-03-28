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

class Solution(object):
    def DFS(self, nestedList, depth):                       #DFS with current depth.
        result = 0
        for x in nestedList:                                #Check each entry in nestedList.
            if x.isInteger():                               #If it's an integer, add its value multiplied by depth to result.
                result += depth * x.getInteger()
            else:                                           #Otherwise, add the return value of DFS with next depth.
                result += self.DFS(x.getList(), depth + 1)
        return result
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.DFS(nestedList, 1)
