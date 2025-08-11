class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        division = 10 ** 9 + 7                                                                  #Initialize division.
        b = format(n, 'b')[::-1]                                                                #Convert n to binary string and reverse it, because the powers array should be sorted in non-desending order.
        prefix_sum = [0]                                                                        #Initialize prefix sum list.
        for i, x in enumerate(b):                                                               #Traverse b.
            if int(x):                                                                          #If current bit is 1, append prefix_sum[-1] + i to prefix_sum list, because each query is product of several power of 2, so we only need the sum of power.
                prefix_sum.append(prefix_sum[-1] + i)
        return [(1 << prefix_sum[r + 1] - prefix_sum[l]) % division for l, r in queries]        #For each query, shift 1 left by the sum of power between powers[left:right + 1] then take the modulo.
