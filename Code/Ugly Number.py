class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:                      #Rule out 0 or negative numbers.
            return False
        while n % 5 == 0:               #Divided it by 5 as many times as it can.
            n //= 5
        while n % 3 == 0:               #Divided it by 3 as many times as it can.
            n //= 3
        while n % 2 == 0:               #Divided it by 2 as many times as it can.
            n //= 2
        return n == 1                   #If the result is 1, it's an ugly number; otherwise, it's not.
