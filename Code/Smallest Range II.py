class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()                                                                                #Sort list.
        minV, maxV = A[0], A[-1]                                                                #Get the min value and max value.
        result = maxV - minV                                                                    #Initalize the result to maxV - minV.
        for i in range(len(A) - 1):                                                             #Traverse the list.
            result = min(result, max(maxV - K, A[i] + K) - min(minV + K, A[i + 1] - K))         #For each pair of adjacent numbers A[i] and A[i + 1], A[i] <= A[i + 1], potential result is max(maxV - K, A[i] + K) - min(minV + K, A[i + 1] - K).
        return result
