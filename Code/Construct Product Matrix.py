class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])                                                                                        #Get the dimensions.
        division = 12345                                                                                                      #Initialize division.
        prefixProduct = [1] * (m * n + 1)                                                                                     #Store the prefix product.
        for i, j in product(range(m), range(n)):                                                                              #Traverse forwards to populate the prefix product.
            prefixProduct[i * n + j + 1] = prefixProduct[i * n + j] * grid[i][j] % division
        suffixProduct = [1] * (m * n + 1)                                                                                     #Store the suffix product.
        for i, j in product(reversed(range(m)), reversed(range(n))):                                                          #Traverse backwards to populate the prefix product.
            suffixProduct[i * n + j] = suffixProduct[i * n + j + 1] * grid[i][j] % division
        return [[prefixProduct[i * n + j] * suffixProduct[i * n + j + 1] % division for j in range(n)] for i in range(m)]     #Return the product matrix by multiply the prefix product before each cell and suffix product after each cell then tale modulo.
