class Solution:
    def maxDiff(self, num: int) -> int:
        digits = str(num)                                                                        #Convert num to string.
        digit_not_9 = None
        for x in digits:                                                                         #Find the first digit that is not 9.
            if x != "9":
                digit_not_9 = x
                break
        max_value = digits.replace(digit_not_9, "9") if digit_not_9 else digits                  #If such digit exists, the max value is replacing all such digits to 9.
        min_value = digits                                                                       #Initialize min value.
        if digits[0] != "1":                                                                     #If the first dught is not 1, replace all same digits with 1 to get the min value.
            min_value = digits.replace(digits[0], "1")
        else:                                                                                    #Otherwise, find the first digit that is not 0 or 1.
            digit_not_1_or_0 = None
            for x in digits:
                if x not in ["0", "1"]:
                    digit_not_1_or_0 = x
                    break
            min_value = digits.replace(digit_not_1_or_0, "0") if digit_not_1_or_0 else digits    #If such digit exists, the min value is replacing all such digits to 0.
        return int(max_value) - int(min_value)                                                   #Return the diff between max value and min value.
