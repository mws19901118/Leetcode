class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):                   #Sieve of Eratosthenes
        if n<=2:
            return 0
        primes=[True for i in range(n)]
        primes[0]=False
        primes[1]=False
        i=2
        while i*i<n:
            if primes[i]:
                j=i*2
                while j<n:
                    primes[j]=False
                    j+=i
            i+=1
        count=0
        for i in range(n):
            if primes[i]:
                count+=1
        
        return count
