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
    def deserialize(self, s: str) -> NestedInteger:
        def dfs(index: int) -> (NestedInteger, int):                    #DFS through s.
            if s[index].isdigit() or s[index] == '-':                   #If s[index] is digit or '-', it is the start of an integer.
                sign = 1                                                #Initialize sign to 1.
                if s[index] == '-':                                     #If s[index] is '-', set sign to -1 and move forward index.
                    sign = -1
                    index += 1
                i = index
                while i < len(s) and s[i].isdigit():                    #Traverse to the end of current integer.
                    i += 1
                return NestedInteger(sign * int(s[index:i])), i         #Return a NestedInteger to be current integer also the current index.
            result = NestedInteger()                                    #Otherwise, it is the start of a list.
            index += 1                                                  #Move forward index.
            while index < len(s) and s[index] != ']':                   #Traverse s until index reaches the end or s[index] is ']'.
                element, index = dfs(index)                             #Recursively deserialize current nested integer.
                result.add(element)                                     #Add element to result.
                if s[index] == ',':                                     #If s[index] is ',', move forward index to go to next element in list.
                    index += 1
            return result, index + 1                                    #Return result and index + 1.
        return dfs(0)[0]                                                #Return the nested integer deserialized from dfs(0).
