class Solution:
    def minOperations(self, s: str) -> int:
        result = len(s)                        #Initialize result.
        for initial in [0, 1]:                 #Check the case of starting with 0 and starting with 1.
            curr, count = initial, 0           #Store initial value and count.
            for x in s:                        #Traverse s.
                count += (int(x) == curr)      #Increase count if int(x) is not curr.
                curr ^= 1                      #XOR curr with 1.
            result = min(result, count)        #Update result if necessary.
        return result
