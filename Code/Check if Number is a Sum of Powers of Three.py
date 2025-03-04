class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:                        #Convert n to a base 3 number.
            if n % 3 == 2:              #If any bit is 2, return false.
                return False
            n //= 3
        return True                     #Return true at the end.
