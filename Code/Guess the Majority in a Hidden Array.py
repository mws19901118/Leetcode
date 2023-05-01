# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()                                                 #Get array length.
        count_equal, count_different, index = 1, 0, -1                      #Since value can only be 0 and 1, count the elements equal to array[0] and count elements different with array[0], also track the index of elements different with array[0](only need one).
        result1234 = reader.query(1, 2, 3, 4)                               #Query 1, 2, 3, 4.
        result0234 = reader.query(0, 2, 3, 4)                               #Query 0, 2, 3, 4.
        if result0234 == result1234:                                        #Since 2, 3, 4 are fixed, by comparing result0234 and result1234, we will know if array[0] equals array[1], updating count and index accordingly.
            count_equal += 1
        else:
            count_different += 1
            index = 1
        result0134 = reader.query(0, 1, 3, 4)                               #Query 0, 1, 3, 4.
        if result0134 == result1234:                                        #Since 1, 3, 4 are fixed, by comparing result0134 and result1234, we will know if array[0] equals array[1], updating count and index accordingly.
            count_equal += 1
        else:
            count_different += 1
            index = 2
        result0124 = reader.query(0, 1, 2, 4)                               #Query 0, 1, 2, 4.
        if result0124 == result1234:                                        #Since 1, 2, 4 are fixed, by comparing result0124 and result1234, we will know if array[0] equals array[1], updating count and index accordingly.
            count_equal += 1
        else:
            count_different += 1
            index = 3
        result0123 = reader.query(0, 1, 2, 3)                               #Query 0, 1, 2, 3.
        for i in range(4, n):                                               #Query 1, 2, 3, i for each i in [4, n - 1].
            x = reader.query(1, 2, 3, i)
            if result0123 == x:                                             #Since 1, 2, 3 are fixed, by comparing result123i and result0123, we will know if array[i] equals array[1], updating count and index accordingly.
                count_equal += 1
            else:
                count_different += 1
                index = i

        if count_equal > count_different:                                   #If count_equal > count_different, array[0] is majority, so return 0.
            return 0
        elif count_equal < count_different:                                 #If count_equal < count_different, array[index] is majority, so return 0.
            return index
        else:                                                               #Otherwose, there is no majority, so return -1.
            return -1
