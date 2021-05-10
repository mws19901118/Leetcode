class Solution:
    def countPrimes(self, n: int) -> int:
        nonprimes = set()                       #Store all non primes from 2 to sqrt(n).
        for p in range(2, int(sqrt(n)) + 1):    #Traverse from 2 to sqrt(n).
            if p not in nonprimes:              #If p is prime, add all numbers which are smaller than n and are multiplier of p to non primes.
                for x in range(p * p, n, p):
                    nonprimes.add(x)
        return max(0, n - len(nonprimes) - 2)   #Return the max of 0 and count of primes, n minus count of non primes minus 2(n itself and 1). 
