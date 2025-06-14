class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = str(num)                                                              #Convert num to string.
        digit_not_9 = None
        for x in digits:                                                               #Find the first digit that is not 9.
            if x != "9":
                digit_not_9 = x
                break
        max_value = digits.replace(digit_not_9, "9") if digit_not_9 else digits        #If such digit exists, the max value is replacing all such digits to 9.
        min_value = digits.replace(digits[0], "0")                                     #Min value is replacing first digit to 0.
        return int(max_value) - int(min_value)                                         #Return the diff between max value and min value.
