from sortedcontainers import SortedList                                                               #SortedList will maintain the list sorted.
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sortedList = SortedList()
        cost = 0
        division = 10 ** 9 + 7
        for x in instructions:                                                                        #Traverse through instructions.
            cost += min(sortedList.bisect_left(x), len(sortedList) - sortedList.bisect_right(x))      #Find the first and last place to insert x in sorted list, let's say A and B. There are A numbers smaller than x and len(sortedList) - B numbers greater than x, so cost to insert x is min(A, len(sortedList) - B).
            cost %= division                                                                          #Calculate modulo.
            sortedList.add(x)                                                                         #Insert x to sortedList.
        return cost
