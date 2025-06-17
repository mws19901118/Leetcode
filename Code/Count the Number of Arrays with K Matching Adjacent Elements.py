class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        def quick_power(x: int, n: int):                                              #Quick power and take modulo.
            result = 1
            while n:
                if n & 1:
                    result = result * x % division
                x = x * x % division
                n >>= 1
            return result
        division = 10 ** 9 + 7                                                        #Initialize division.
        return m * comb(n - 1, k) * quick_power(m - 1, n - 1 - k) % division          #First position has m choices then choose k positions in the rest n - 1 positions and fix them to be same as their previous position respectively.
                                                                                      #Next, for the rest n - 1 - k positions, each has m - 1 choices because they are not allowed to be same as their previous position.
