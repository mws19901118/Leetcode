class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        row = len(A)
        col = len(A[0])
        for i in range(col):
            for j in range(1, row):
                if A[j][i] < A[j - 1][i]:   #For each row, if there is a character smaller than previous one, add 1 to count.
                    count += 1
                    break
        return count
