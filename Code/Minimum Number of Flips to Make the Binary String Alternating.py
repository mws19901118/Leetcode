class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)                                                        #Get the string length.
        flip0 = sum(int(x) ^ 0 ^ (i & 1) for i, x in enumerate(s))        #Count the flips to flip string to alternating string starting with '0'.
        result = min(flip0, n - flip0)                                    #Initialize result to flip string to alternating string starting with either '0' or '1'(flips to start with '1' is just the inverse of flips to start with '0')..
        if not n & 1:                                                     #If the n is even, type-1 operation has no effect, because it doesn't change the relative differnece of '0' and '1' on odd and even indexes.
            return result
        for x in s:                                                       #Traverse s to simulate type-1 operation after each digit.
            flip0 = n - flip0 + (1 if int(x) else -1)                     #Update flip0 based on current digit value. See the proof below.
            result = min(result, flip0, n - flip0)                        #Update result if necessary.
        return result
                                                                          #Proof:
                                                                          #Initially, let's assume at any given point, there are x '0' on even indexes, y '0' on odd indexes, u '1' on even indexes and v '1' on odd indexes, so we need to flip '0' on odd indexes and '1' on even indexes to make string alternating string starting with '0'.
                                                                          #Thus, flip0 = y + u = n - x - v.
                                                                          #For case 0, if the first digit is '0', simulate the type-1 operation.
                                                                          #It will move digits on even indexes to odd indexes and vice versa.
                                                                          #Now there are x - 1 '0' on odd inedxes after removing first digit and y + 1 '0' on even indexes after appending first digit to the end(the end is always even index because the n is odd).
                                                                          #Now there are u '1' on odd indexes and v '1' on even indexes.
                                                                          #So the new flip 0 flip0' = x - 1 + v = n - flip0 - 1.
                                                                          #For case 1, if the first digit is '1', simulate the type-1 operation.
                                                                          #It will move digits on even indexes to odd indexes and vice versa.
                                                                          #Now there are x '0' on odd inedxes and y '0' on even indexes.
                                                                          #Now there are u - 1 '1' on odd inedxes after removing first digit and v + 1 '1' on even indexes after appending first digit to the end(the end is always even index because the n is odd).
                                                                          #So the new flip 0 flip0' = x + v + 1 = n - flip0 + 1.
                                                                          #Finally, flip0' = n - flip0 + (1 if int(x) else -1).
