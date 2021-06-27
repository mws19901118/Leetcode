from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums):
        sortedList, result = SortedList(), []                   #Use SortedList to maintain the numbers after current number in ascending order.
        for x in nums[::-1]:                                    #Traverse nums reversely.
            index = SortedList.bisect_left(sortedList, x)       #Find the place to insert in sorted list using binary search, which is the count of smaller number of current number.
            result.append(index)                                #Add the index to result.
            sortedList.add(x)                                   #Add current number to sorted list.
        return result[::-1]                                     #Return the reverse of result.
