class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([x for x in range(2, right.bit_length() + 1) if all(x % j for j in range(2, int(sqrt(x)) + 1))])    #Find all the primes between 2 and right.bit_length().
        return sum(int(i.bit_count() in primes) for i in range(left, right + 1))                                         #Count the numbers with prime set of bit from left to right.
