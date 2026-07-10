class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        division = 10 ** 9 + 7                                                                                                                    #Initialize division.
        power10 = [1] * (len(s) + 1)                                                                                                              #Initialize and populate each power of 10(from 0 to len(s)) after taking modulo.
        for i in range(1, len(s) + 1):
            power10[i] = power10[i - 1] * 10 % division
        prefixSum, x, count = [0], [0], [0]                                                                                                       #Initialize the prefix sum of digits, x, and count of non-zero digits at each index.
        for i, c in enumerate(s):                                                                                                                 #Traverse s and populate prefixSum, x and count.
            d = int(c)
            prefixSum.append(prefixSum[-1] + d)
            x.append((x[-1] * 10 + d) % division if d > 0 else x[-1])
            count.append(count[-1] + (d > 0))
        return [(x[v + 1] - x[u] * power10[count[v + 1] - count[u]]) * (prefixSum[v + 1] - prefixSum[u]) % division for u, v in queries]          #Traverse queries and calculate the result of each query.
                                                                                                                                                  #For each query u and v, the sum part is easily prefixSum[v + 1] - prefixSum[u].
                                                                                                                                                  #Then we need to calculate the x for this query.
                                                                                                                                                  #x[u] is a prefix of x[v + 1], we actually want the suffix part.
                                                                                                                                                  #Since the length of suffix is count[v + 1] - count[u], the suffix is x[v + 1] - x[u] * 10 ** (ocunt[v + 1] - count[u]).
                                                                                                                                                  #Since we already calculated the modulo of power of 10 and and the formula is polynomial, then use power10[count[v + 1] - count[u]].
                                                                                                                                                  #Next calculate the product and take modulo.
