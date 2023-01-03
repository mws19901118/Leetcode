class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])                                                                      #Get dimensions.
        return sum(any(strs[j][i] > strs[j + 1][i] for j in range(m - 1)) for i in range(n))                #Return the count of columns that are not sorted.
