class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0                     #Count the index of current factor.
        for i in range(1, n + 1):     #Traverse from 1 to n.
            if n % i == 0:            #If i is a factor, increase count by 1.
                count += 1
            if count == k:            #If count == k, return i.
                return i
        return -1                     #Return -1 if not found.
