class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefixSum = [0]                                                                        #Initialize prefix sum for the overall profit at each day.
        for p, s in zip(prices, strategy):                                                     #Traverse prices and strategy simultaneously to populate the prefix sum.
            prefixSum.append(prefixSum[-1] + p * s)
        window = sum(prices[(k + 1) // 2:k])                                                   #Calculate the profit after performing modification on the first k days, which is the sum of second half. 
        result = max(prefixSum[-1], prefixSum[-1] + window - prefixSum[k])                     #Initialize the result to be the greater of original profit and modification on the first k days, delta is window - prefixSum[k].
        for i in range(1, len(prices) - k + 1):                                                #Traverse the start of rest possible modifications.
            window += prices[i + k - 1]                                                        #Add prices[i + k - 1] to window.
            window -= prices[i + (k - 1) // 2]                                                 #Remove prices[i + (k - 1) // 2] from window.
            result = max(result, prefixSum[-1] + window - prefixSum[i + k] + prefixSum[i])     #Update result if current profit is higher, delta is window - (prefixSum[i + k] - prefixSum[i]).
        return result
