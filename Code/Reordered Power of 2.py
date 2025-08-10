class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)                                                                                      #Covert N to string.
        lower, upper = ceil(log2(10 ** (len(s) - 1))), floor(log2(10 ** len(s) - 1))                    #Find the lower and upper bound of power so that the power of 2 will have the same length with N.
        count = Counter(s)                                                                              #Count each digit in N.
        power = 1 << lower
        for i in range(lower, upper + 1):                                                               #Traverse all the power of 2 from 2 ** lower to 2 ** upper.
            if Counter(str(power)) == count:                                                            #If current power of 2 has same digit distribution with N, then it can be form by reordering N, so return True.
                return True
            power <<= 1
        return False                                                                                    #Return false if such power of 2 not found.
