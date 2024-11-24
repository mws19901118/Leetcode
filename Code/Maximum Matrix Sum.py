class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])                                  #Get the dimensions.
        non_positive_count, abs_min, abs_sum = 0, inf, 0                    #Initialize the non-positive number count, minimum of abs of each number and sum of abs of each number.
        for i, j in product(range(m), range(n)):                            #Traverse matrix.
            non_positive_count += int(matrix[i][j] <= 0)                    #Update non_positive_count.
            abs_min = min(abs_min, abs(matrix[i][j]))                       #Update abs_min.
            abs_sum += abs(matrix[i][j])                                    #Update abs_sum.
        return abs_sum - (abs_min if non_positive_count & 1 else 0) * 2     #Since we can move the non-positive sign inside matrix without modifying the count of non-negative numbers. So, just move all non-positive signs into adjacent areas.
                                                                            #Next flip them: if the count of non-positive sign is even, we can flip all of them to non-negative and the result is abs_sum; otherwise, there is one left and desinate it to be the number of abs_min, so the result is abs_sum - abs_min * 2.
