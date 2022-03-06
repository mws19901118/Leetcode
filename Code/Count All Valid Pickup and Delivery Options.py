class Solution:
    def countOrders(self, n: int) -> int:
        divisor = 10 ** 9 + 7                             #Initialize division.
        count = 1                                         #Initialize count for n = 1.
        for i in range(2, n + 1):                         #Iterate from 2 to n.
            count = count * (2 * i - 1) * i % divisor     #The length of sequence from i - 1 is 2 * (i - 1), so there are 2 * (i - 1) - 1 places to put a new pickup and for each pickup placed, let's say at j-th place(0 indexed from beginning), there are 2 * (i - 1) - 1 - j places to put a new delivery.
        return count                                      #Thus, in total, there are (2 * i - 1) * i more ways in this iteration. Calculate the remain and return the final result.
