class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = []
        while n:                                                                #Convert n to a list of digits in reversed order.
            digits.append(n % 10)
            n //= 10
        index = 1
        while index < len(digits) and digits[index] >= digits[index - 1]:       #Find the first digit, let's say X, that is smaller than previous digit(from front to back in list i.e. from back to front in n).
            index += 1
        if index == len(digits):                                                #If no such X, digits of n is in non-ascending order and it's already the greatest. So, return -1.
            return -1
        newDigits = []                                                          #Create a list to store digits for next greater element(from front to back).
        newDigits.extend(reversed(digits[index + 1:]))                          #Add the digits in reversed order after X to new digits. They are the common unchanged prefix in both n and next greater element.
        i = 0
        while i < index and digits[i] <= digits[index]:                         #Find the first digit that is greater than X we found above.
            i += 1
        newDigits.append(digits[i])                                             #Add it to new digits, thus the new element is greater than n.
        newDigits.extend(digits[:i])                                            #Add digits before it to new digits; they are not greater than X, so new element is the smallest that greater than n.
        newDigits.append(digits[index])                                         #Add X to new digits.
        newDigits.extend(digits[i + 1:index])                                   #Add the remaining digits to new digits; they are greater than X.
        result = 0                                                              #Covert it to int.
        for d in newDigits:
            result = result * 10 + d
        if result > 0x7FFFFFFF:                                                 #If result exceeds 32-bit integer max, return -1.
            return -1
        return result                                                           #Return result.
