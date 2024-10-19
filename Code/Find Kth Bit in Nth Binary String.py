class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:                                                            #If n is 1, return "0" directly.
            return "0"
        length = (1 << n) - 1                                                 #Calculate the length of nth binary string.
        mid = (length + 1) // 2                                               #Calculate the mid index(starting from 1).
        if k == mid:                                                          #If k is mid, return "1".
            return "1"
        elif k < mid:                                                         #If k < mid, return the kth bit in (n - 1)th binary string.
            return self.findKthBit(n - 1, k)
        else:                                                                 #If k > mid, find the reverse kth bit in (n - 1)th binary string, then inverse.
            return str(1 - int(self.findKthBit(n - 1, length - k + 1)))
