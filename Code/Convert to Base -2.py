class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:                                        #If n is 0, return "0".
            return "0"
        result = ""                                       #Initialize return.
        while n != 0:                                     #Iterate to convert n to base -2 until n is 0.
            n, remainder = divmod(n, -2)                  #Get the quotient and remainder of n divided by -2.
            if remainder < 0:                             #If remainder is 0, since we can only have positive digit in result, increase n by 1 and increase remainder by 2. n * -2 + d = (n + 1) * -2 + d + 2.
                n, remainder = n + 1, remainder + 2
            result = str(remainder) + result              #Add the remainder at the start of result.
        return result
