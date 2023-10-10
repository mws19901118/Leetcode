class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        division = 10 ** 9 + 7                                                              #Initialize division.
        @cache                                                                              #Cache result.
        def dp(length: int, maxValue: int, cost: int) -> int:                               #Use DP to calculate the number of ways of building arrays with given length, max value and search cost.
            if maxValue < cost or length < cost:                                            #If max value of length is smaller than cost, return 0 because max search cost is not greater than length or max value.
                return 0
            if length == 1:                                                                 #If length is 1, return 1, i.e. [1].
                return 1
            result = dp(length - 1, maxValue, cost) * maxValue                              #First case is last number does not increase search cost. So, the max value has appeared before last number. There are dp(length - 1, maxValue, cost) ways to build such length - 1 arrays, and we can put any number between 1 and maxValue at last number.
            if cost > 1:                                                                    #Second case is last number increases search cost, and cost is greater than 1(search cost will be at least 1 when traversing array).
                result += sum(dp(length - 1, i, cost - 1) for i in range(1, maxValue))      #Thus, max value has to appear first time at last number. Sum up the ways of that: dp(length - 1, i, cost - 1) for i in [1: maxValue].
            return result % division                                                        #Return the modulo.
        return sum(dp(n, i, k) for i in range(1, m + 1)) % division                         #Sum up dp(n, i, k) for i in [1:m + 1], basically enumerating the possible max values. And then return the modulo.
