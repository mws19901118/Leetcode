class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:                                                #Same as Total Waviness of Numbers in Range I.py
        def calculateTrend(a: int, b: int) -> int:
            return 1 if b > a else (-1 if b < a else 0)

        def isPeakOrValley(incoming: int, outgoing: int) -> bool:
            return incoming and outgoing and incoming != outgoing

        @cache
        def dp(first: int, length: int, trend: int) -> int:
            if length == 1:
                return 0
            result = 0
            for i in range(0, 10):
                newTrend = calculateTrend(first, i)
                if isPeakOrValley(trend, newTrend):
                    result += 10 ** (length - 2)
                result += dp(i, length - 1, newTrend)
            return result

        def count(num: int) -> int:
            digits = [int(c) for c in str(num)]
            n = len(digits)
            result = 0
            for length in range(1, n):
                result += sum(dp(i, length, 0) for i in range(1, 10))
            trend = 0
            for i, x in enumerate(digits):
                start = 1 if not i else 0
                for d in range(start, x):
                    newTrend = 0 if not i else calculateTrend(digits[i - 1], d)
                    if isPeakOrValley(trend, newTrend):
                        result += 10 ** (n - i - 1)
                    result += dp(d, n - i, newTrend)
                if i > 0:
                    newTrend = calculateTrend(digits[i - 1], x)
                    if isPeakOrValley(trend, newTrend):
                        result += sum(digits[j] * 10 ** (n - 1 - j) for j in range(i + 1, n)) + 1
                    trend = newTrend
            return result

        return count(num2) - count(num1 - 1)
