#To compute the number of k inverse pairs array of size n, noted as dp(n, k), suppose we have already computed dp(n - 1, i) and i is from 0 to k.
#Then, what we need to insert number n to the permutation arrays of numbers from 1 to n - 1.
#Because n is the largest number now, if insert before i number, it will generate i new inverse pairs.
#Thus, dp(n, k) = sum of dp(n - 1, k - i), i in [0, 1, ..., min(k, n - 1)].
#Furthermore, since dp(n, k - 1) = sum of dp(n - 1, k - 1 - i), i in [0, 1, ..., min(k - 1, n - 1)], dp(n, k) = dp(n, k - 1) + dp(n - 1, k) - (dp(n - 1, k - n) if k >= n).
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        division = 10 ** 9 + 7                                                                        #Initialize division.
        dp = [0] * (k + 1)                                                                            #Initialize dp array for n = 0, if n == 0, there is no inverse pairs array for any k.
        for i in range(1, n + 1):                                                                     #Traverse from 1 to n.
            nextdp = [1] + [0] * k                                                                    #Initialize dp array for current n; if k is 0, there can only be 1 array with 0 inverse pair, which is the sorted in ascending order array.
            for j in range(1, min(k, i * (i - 1) // 2) + 1):                                          #Traverse from 1 to min(k, i * (i + 1) // 2), because an array with size i can have at most i * (i + 1) // 2 inverse pairs, which is the sorted in desending order array.
                nextdp[j] = (nextdp[j - 1] + dp[j] - (dp[j - i] if j >= i else 0)) % division         #Update nextdp[j] according to the state transition equation, dp(n, k) = dp(n, k - 1) + dp(n - 1, k) - (dp(n - 1, k - n) if k >= n).
            dp = nextdp                                                                               #Replace dp with nextdp.
        return dp[-1]                                                                                 #Return dp[-1], which is dp(n, k).
