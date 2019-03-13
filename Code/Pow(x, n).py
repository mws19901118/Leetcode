class Solution:
    def myPow(self, x: float, n: int) -> float:
        b = format(abs(n), '0b')                                #Convert the abs value of n to binary.
        p = [1, x]                                              #Use a list to store the powers of x. Initially, x^0 and x^1.
        while len(p) <= len(b):                                 #While the length of p is not larger than that of b, keep expanding p so the new power is the square of previous power.
            p.append(p[-1] * p[-1])
        
        result = 1                                              #Initalize result to be 1.
        for i in range(len(b) - 1, -1, -1):                     #Traverse through b.
            if b[i] == '1':                                     #If current bit is '1', multiply result with its corrsponding power(notice the order in p).
                result *= p[len(b) - i]
        if n < 0:                                               #If n is negative, let result be its reciprocal.
            result = 1 / result
        return result
