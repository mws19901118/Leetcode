class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        matrix = [[inf for _ in range(26)] for _ in range(26)]                                                            #Build graph.
        for i in range(26):
            matrix[i][i] = 0
        for x, y, c in zip(original, changed, cost):
            matrix[ord(x) - ord('a')][ord(y) - ord('a')] = min(c, matrix[ord(x) - ord('a')][ord(y) - ord('a')])           #Since there could be multiple costs for same pair, take the smallest one.
        for k, i, j in product(range(26), range(26), range(26)):                                                          #Use floyd-warshall algorithm to precompute the cost from one character to another.
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]
        result = 0
        for x, y in zip(source, target):                                                                                  #Traverse source and target simultonously.
            if matrix[ord(x) - ord('a')][ord(y) - ord('a')] == inf:                                                       #If cannot convert current pair, return -1.
                return -1
            result += matrix[ord(x) - ord('a')][ord(y) - ord('a')]                                                        #Add cost to result.
        return result
