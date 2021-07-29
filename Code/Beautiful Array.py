class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        array = [1]                                                         #Initialize array for n == 1.
        while len(array) < n:                                               #Iterate while array length is smaller than n.
            array = [2 * x - 1 for x in array] + [2 * x for x in array]     #Current array is already beautiful, so map current array from positive integer to positive odd integer on the left part and to positive even integer on the right part.
        return [x for x in array if x <= n]                                 #Because current array is already beautiful, both new left part and right part is beautiful and the sum of each intersection pair(one integer from left and one integer from right) is odd, so it can't be the double of any integer between them.
                                                                            #Thus new array is also beautiful. Return the integers in array which are not larger than n while preseving the order.
