class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeFactors = set()                                  #Store prime factors in a set.
        for num in nums:                                      #Traverse nums.
            x = num                                           #Set x to be num.
            for i in range(2, ceil(sqrt(num)) + 1):           #Traverse from 2 to the ceil of root of num.
                while x % i == 0:                             #While i can divide x, add i to prime factors and divide x by i.
                    primeFactors.add(i)
                    x //= i
            if x > 1:                                         #If x is still greater than 1, x is a prime and add it to prime factors.
                primeFactors.add(x)
        return len(primeFactors)                              #Return the length of prime factors.
