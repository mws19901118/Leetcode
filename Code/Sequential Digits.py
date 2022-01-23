class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result, digits = [], [1,2,3,4,5,6,7,8]                      #Initialize result and starting digits.
        while digits and digits[0] <= high:                         #BFS until digits is empty or the smallest number in digits is greater than high.
            newDigits = []                                          #Initialize new digits.
            for x in digits:                                        #Traverse digits.
                if low <= x <= high:                                #If x is within range, append it to result.
                    result.append(x)
                lastDigit = x % 10                                  #Get the last digit of x.
                if lastDigit != 9:                                  #If x is not 9, append the next sequential digit to new digits.
                    newDigits.append(x * 10 + lastDigit + 1)
            digits = newDigits                                      #Replace digits with newDigits.
        return result
