class Solution:
    def countGoodNumbers(self, n: int) -> int:
        division = 10 ** 9 + 7                                                          #Initialize division.
        def quick_power(x: int, y: int) -> int:                                         #Quick computing of x ** y * division.
            result = 1                                                                  #Initialize result to 1.
            while y > 0:                                                                #Iterate while y > 0.
                if y & 1:                                                               #If the current last digit of y is 1, multiple result by x then calculate the modulo.
                    result = result * x % division
                multiplier = x * x % division                                           #Update x to x * x then calculate the modulo.
                y >>= 1                                                                 #Right shift y by 1 digit. 
            return result

        return quick_power(5, (n + 1) // 2) * quick_power(4, n // 2) % division         #There will be (n + 1) // 2 even digits and n // 2 odd digits, so return 5 ** ((n + 1) // 2) * 4 ** (n // 2) then calculate the modulo.
