class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0                                  #Initialize result/
        for x in nums:                              #Traverse nums.
            count, s = 0, 0                         #Initialize count and sum of divisors.
            for i in range(1, int(sqrt(x)) + 1):    #Traverse from 1 to the square root of x.
                if not x % i:                       #If i is a divisor of x, increase count and add i to s.
                    count += 1
                    s += i
                    j = x // i                      #Also calculate x // i.
                    if j != i:                      #If j does not equal i, increase count and add j to s.
                        count += 1
                        s += j
            if count == 4:                          #If there are exactly 4 divisors, add s to result.
                result += s
        return result
