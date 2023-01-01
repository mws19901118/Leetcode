class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        digits = [int(x) for x in s]                                        #Convert s to digits.
        count, i = 0, 0                                                     #Initialize count and a pointer.
        while i < len(digits):                                              #Traverse digits.
            partition, j = 0, i                                             #Initialize a new partition and pointer j to be i.
            while j < len(digits) and partition * 10 + digits[j] <= k:      #While the partition value is not greater than k, add digits[j] to partition and increase j.
                partition = partition * 10 + digits[j]
                j += 1
            if j == i:                                                      #If j == i, then digits[i] is greater than k, so cannot generate a new partition then return -1.
                return -1
            i = j                                                           #Set i to j.
            count += 1                                                      #Increase count.
        return count                                                        #Return count.
