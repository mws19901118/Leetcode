class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        division = 10 ** 9 + 7                                                                          #Initialize the division.
        m = r - l + 1                                                                                   #Get the length of possible digits.
        dp0, dp1 = [1] * m, [1] * m                                                                     #Initialize the base case for zigzag array trending down and trending up.
        for _ in range(n - 1):                                                                          #Iterate n - 1 times.
            sum0, sum1 = list(accumulate(dp0, initial = 0)), list(accumulate(dp1, initial = 0))         #Calculate the prefix sum of dp0 and dp1 respectively.
            dp0 = [x % division for x in sum1[:-1]]                                                     #New dp0 is the prefix sum of dp1 at each digit.
            dp1 = [(sum0[-1] - x) % division for x in sum0[1:]]                                         #New dp1 is the prefix sum from the other side of dp0 at each digit.
        return (sum(dp0) + sum(dp1)) % division                                                         #Sum up dp0 and dp1, take modulo then return.
