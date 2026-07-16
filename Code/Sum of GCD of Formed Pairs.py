class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxV = 0
        prefixGcd = []
        for x in nums:                                                                            #Iterate nums.
            maxV = max(maxV, x)                                                                   #Update max value.
            prefixGcd.append(gcd(x, maxV))                                                        #Populate prefix GCD.
        prefixGcd.sort()                                                                          #Sort prefix GCD.
        return sum(gcd(prefixGcd[i], prefixGcd[-(i + 1)]) for i in range(len(prefixGcd) // 2))    #Return the sum of GCD of formed pairs.
