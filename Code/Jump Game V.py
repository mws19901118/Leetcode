class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @cache                                                                      #Cache result.
        def dp(index: int) -> None:                                                 #DP to find the max indexes can visit from current index.
            result = 1                                                              #Initialize result to be 1.
            i = index - 1
            while i >= 0 and index - i <= d and arr[index] > arr[i]:                #Traverse left until cannot reach.
                result = max(result, dp(i) + 1)                                     #Calculate dp(i) and update result if necessary.
                i -= 1
            i = index + 1
            while i < len(arr) and i - index <= d and arr[index] > arr[i]:          #Traverse left until cannot reach.
                result = max(result, dp(i) + 1)                                     #Calculate dp(i) and update result if necessary.
                i += 1
            return result

        return max(dp(i) for i in range(len(arr)))                                  #Return the max result of dp(i) for each index in arr.
