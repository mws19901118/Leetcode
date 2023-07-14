class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengthByEndValue = defaultdict(int)                                                            #Store the longest arithmetic subarray length ending at each number.
        for x in arr:                                                                                  #Traverse arr.
            lengthByEndValue[x] = max(lengthByEndValue[x], lengthByEndValue[x - difference] + 1)       #x forms an arithmetic subarray with all sarithmetic subarray ending at x - difference; update lengthByEndValue[x].
        return max(lengthByEndValue.values())                                                          #Return the max of values of lengthByEndValue.
