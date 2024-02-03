class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache                                                                        #Cache result.
        def dp(index: int) -> int:                                                    #Return the max sum of partitioning arr[index:].
            current_max, result = 0, 0                                                #Initialize current max and result.
            for i in range(index, min(index + k, len(arr))):                          #Traverse from index to index + k - 1 or the end of arr.
                current_max = max(current_max, arr[i])                                #Update current max.
                result = max(result, current_max * (i - index + 1) + dp(i + 1))       #Calculate max sum of current partition: sum of current subarray plus the result of dp(i + 1). Then update result if necessary.
            return result
        return dp(0)                                                                  #Return the result of dp(0).
