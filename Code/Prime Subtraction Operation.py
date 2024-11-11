class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_value = max(nums)                                              #Get the max value in nums.
        sieve = [1] * (max_value + 1)                                      #Find if numbers from 0 to max_value are prime.
        sieve[1] = 0
        for i in range(2, int(sqrt(max_value + 1)) + 1):
            if sieve[i]:
                for j in range(i * i, max_value + 1, i):
                    sieve[j] = 0
        max_primes, index = [0], 0                                         #Find the max prime smaller than or equal to each number from 0 to max_value.
        for i in range(1, max_value + 1):
            max_primes.append(max_primes[-1] if not sieve[i] else i)
        prev = 0                                                           #Initialize the value of previous index after operation.
        for x in nums:                                                     #Traverse nums.
            if x <= prev:                                                  #If current number is not greater than perv, return false.
                return False
            prev = x - max_primes[x - prev - 1]                            #x can be reduced to at least prev + 1, so we the room to reduce is x - prev - 1, and is exactly max_primes[x - prev - 1].
        return True                                                        #Return true at the end.
