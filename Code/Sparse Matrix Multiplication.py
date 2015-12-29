class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        if m == 0:
            return []
        n = len(A[0])
        if n == 0:
            return []
        k = len(B[0])
        if k == 0:
            return []
        newA = [[] for i in range(m)]                     #Store every row of A.
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    newA[i].append((j, A[i][j]))          #In each row, store every non-zero elements as a tuple (j, A[i][j]).
        AB = [[0 for j in range(k)] for i in range(m)]
        for i in range(m):                                #Calculate AB.
            for x in newA[i]:
                for j in range(k):
                    AB[i][j] += x[1]*B[x[0]][j]
        return AB
