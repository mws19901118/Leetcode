class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):                              #Enumerate a.
            for b in range(a + 1, n + 1):                      #Enumerate b such that b > a.
                c = sqrt(a * a + b * b)                        #Calculate c.
                if c <= n and abs(c - int(c)) <= 0.000001:     #If c is not greater than n and is an integer, increase count by 2(triplet abc and triplet bac).
                    count += 2
        return count
