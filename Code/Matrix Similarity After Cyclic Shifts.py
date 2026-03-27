class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])                                                                                  #Get the dimensions.
        k %= n                                                                                                        #Replace k with the modulo after divided by n.
        return all(all(mat[i][j] == mat[i][(j + (k if i & 1 else -k)) % n] for j in range(n)) for i in range(m))      #Simulate the shift process each row and make sure the row is same as before.
