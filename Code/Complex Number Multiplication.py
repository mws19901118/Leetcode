class Solution:
    def parse(self, num: str):                                                                                  #Parse complex number.
        s = num.split("+")                                                                                      #Split by '+'.
        return int(s[0]), int(s[1][:-1])                                                                        #The number before '+' is real; the number after '+' is imaginary(exclude 'i').
    
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = self.parse(num1)                                                                    #Parse num1.
        real2, imaginary2 = self.parse(num2)                                                                    #Parse num2.
        real, imaginary = real1 * real2 - imaginary1 * imaginary2, real1 * imaginary2 + real2 * imaginary1      #Calculate result.
        return str(real) + "+" + str(imaginary) + "i"                                                           #Convert result to complex number string.
