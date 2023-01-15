# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        def trinarySearch(start: int, end: int) -> int:                                   #Trinary search.
            if start == end:                                                              #If start and end is same, we found the index, return it.
                return start
            size = (end - start) // 3                                                     #Divide the array[start..end] into 3 subs with approximately same size.
            compare = reader.compareSub(start, start + size, end - size, end)             #Compare the first sub and last sub.
            if compare == 1:                                                              #If first sub is larger, keep trinary serach in first sub.
                return trinarySearch(start, start + size)
            elif compare == -1:                                                           #If last sub is larger, keep trinary search in last sub.
                return trinarySearch(end - size, end)
            else:                                                                         #If they are equal, keep trinary serach in middle sub.
                return trinarySearch(start + size + 1, end - size - 1)

        return trinarySearch(0, reader.length() - 1)                                      #Return the trinary serach result of the whole array.
