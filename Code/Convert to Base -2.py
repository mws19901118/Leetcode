class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:                            #If n is 0, return "0".
            return "0"
        result = ""                           #Initialize return.
        while n != 0:                         #Iterate to convert n to base -2 until n is 0.
            r = n % 2                         #Get the remainder after dividing by 2.
            result = str(r) + result          #Add the dight at the start of result.
            n = -(n // 2)                     #Replace n with the opposite value of quotient divided by 2.
        return result
