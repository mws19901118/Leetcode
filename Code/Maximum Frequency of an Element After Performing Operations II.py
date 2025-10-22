class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = Counter(nums)                                                       #Count each number.
        prefixSum = Counter()                                                       #Initialize prefix sum contribution.
        for x in count:                                                             #Traverse count.
            prefixSum[x - k] += count[x]                                            #x can contribute count[x] to prefix sum at x - k.
            prefixSum[x + k + 1] -= count[x]                                        #The contribution is gone at x + k + 1.
        values = sorted(prefixSum.keys() | count.keys())                            #Sort all possible values(keys in count and keys in prefix sum).
        result, total = 0, 0                                                        #Initialize result and total possible contribution so far.
        for x in values:                                                            #Traverse values.
            total += prefixSum[x]                                                   #Update total.
            result = max(result, count[x] + min(total - count[x], numOperations))   #Since the operation has a limit, we can update at most min(total - count[x], numOperations) numbers to x. Thus update result if count[x] + min(total - count[x], numOperations) is larger.
        return result
