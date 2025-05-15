import numpy as np                                                                      #Import numpy.
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:       #Since each transformation is independent and the transformation result for each letter is fixed, we can build a transition matrix.
        def matrix_power_mod(matrix: np.ndarray, power: int) -> np.ndarray:             #Fast matrix exponential.
            result = np.identity(n, dtype = object)                                     #Create a new identity matrix.
            while power:                                                                #Iterate while power is greater than 0.
                if power & 1:                                                           #If the last bit of current power is 1, multiple result by matrix then take modulo for each element.
                    result = (result @ matrix) % division
                matrix = (matrix @ matrix) % division                                   #Update matrx to matrx * matrix then take modulo for each element.
                power >>= 1                                                             #Right shift power by 1 bit.
            return result

        division, n = 10 ** 9 + 7, 26                                                   #Initialize division and length of matrix.
        transition_matrix = np.zeros((n, n), dtype = object)                            #Initialize transition matrix to a n * n numpy 2d array with data type object to avoid overflow.
        for i in range(n):                                                              #Traverse each letter, 
            for j in range(nums[i]):                                                    #Traverse nums[i].
                transition_matrix[(i + 1 + j) % 26][i] = 1                              #Populate the transition matrix for current letter.
        final_matrix = matrix_power_mod(transition_matrix, t)                           #Apply the fast matrix exponential on transition matrix with power t.
        sums = np.sum(final_matrix, axis = 0) % division                                #Sum up the final matrix by column(i.e., final result of each letter) then take modulo.
        return sum(sums[ord(x) - ord('a')] for x in s) % division                       #Sum up the sums for each letter in s, then take modulo and return.
