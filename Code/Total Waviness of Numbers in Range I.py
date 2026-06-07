class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculateTrend(a: int, b: int) -> int:                                                                  #Calculate the trend from a to b, return 1 if a < b, -1 if a > b or 0 if a == b.
            return 1 if b > a else (-1 if b < a else 0)

        def isPeakOrValley(incoming: int, outgoing: int) -> bool:                                                   #Given the incoming trend and outgoing trend of the same digit, determine if it is a peak or valey: both trends cannot be 0 and not equal to each other.
            return incoming and outgoing and incoming != outgoing

        @cache                                                                                                      #Cache result.
        def dp(first: int, length: int, trend: int) -> int:                                                         #Calculate the total waviness of all numbers of given length and first digit, and the incoming trend to the first digit.
            if length == 1:                                                                                         #If only 1 digit, return 0.
                return 0
            result = 0
            for i in range(0, 10):                                                                                  #Traverse from 0 to 9.
                newTrend = calculateTrend(first, i)                                                                 #Calculate the outgoing trend from first digit.
                if isPeakOrValley(trend, newTrend):                                                                 #If the first digit is a peak or valley, add 10 ** (length - 2) because there are 10 ** (length - 2) numbers starting with this peak or valley.
                    result += 10 ** (length - 2)
                result += dp(i, length - 1, newTrend)                                                               #Go to next digit and add dp(i, length - 1, newTrend) to result.
            return result

        def count(num: int) -> int:                                                                                 #Count the total waviness from 1 to num.
            digits = [int(c) for c in str(num)]                                                                     #Convert num to digits.
            n = len(digits)                                                                                         #Get the length.
            result = 0
            for length in range(1, n):                                                                              #Sum up waviness of all numbers with fewer digits than num.
                result += sum(dp(i, length, 0) for i in range(1, 10))
            trend = 0                                                                                               #Process n-digit numbers up to num; first initialize the trend.
            for i, x in enumerate(digits):                                                                          #Traverse digits.
                start = 1 if not i else 0                                                                           #Set start to 0 if not first digit; otherwise 1.
                for d in range(start, x):                                                                           #Traverse from start to x - 1, basically the numbers smaller than num at current digit.
                    newTrend = 0 if not i else calculateTrend(digits[i - 1], d)                                     #Calculate the new trend into d.
                    if isPeakOrValley(trend, newTrend):                                                             #If digits[i - 1](must be valid since if i == 0, both trend and new trend is 0) is a peak or valley, add 10 ** (n - i - 1) to result because all remaining numbers with same prefix num[:i] + d will have the wave.
                        result += 10 ** (n - i - 1)
                    result += dp(d, n - i, newTrend)                                                                #Add dp(d, n - i, newTrend) to result for waviness in the last n - 1 digits of all remaining numbers with same prefix num[:i] + d.
                if i > 0:                                                                                           #If i > 0, we also need to process the numbers on the edge(with prefix num[:i + 1]).
                    newTrend = calculateTrend(digits[i - 1], x)                                                     #Calculate the new trend into x.
                    if isPeakOrValley(trend, newTrend):                                                             #If digits[i - 1] is a peak or valley, add the remaining numbers with prefix num[:i + 1] to result as because they all have the wave.
                        result += sum(digits[j] * 10 ** (n - 1 - j) for j in range(i + 1, n)) + 1
                    trend = newTrend                                                                                #Replace trend with new trend.
            return result

        return count(num2) - count(num1 - 1)                                                                        #Return count(num2) - count(num1 - 1).
