class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [x for x in str(n)]                           #Convert n to digits as strings.
        i = len(s) - 1
        while i >= 1 and s[i] <= s[i - 1]:                #Traverse from behind to find the first i such that s[i] > s[i - 1].
            i -= 1
        if not i:                                         #If no such i, digits are already sorted in desending order, then there is no next greater element, so return -1.
            return -1
        j = len(s) - 1
        while j >= i and s[j] <= s[i - 1]:                #Traverse from behind to find the first j such that s[j] > s[i - 1].
            j -= 1
        s[i - 1], s[j] = s[j], s[i - 1]                   #Swap s[j] and s[i - 1].
        s[i:] = s[i:][::-1]                               #Reverse s[i:].
        result = int("".join(s))                          #Join the digits and convert it to int.
        return result if result <= 2 ** 31 - 1 else -1    #If result exceeds 32-bit integer max, return -1; otherwise, return result.
