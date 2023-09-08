class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]                                                                                                #Initialize result.
        for _ in range(numRows - 1):                                                                                  #Iterate numRows - 1 times.
            result.append([1] + [result[-1][i] + result[-1][i + 1] for i in range(len(result[-1]) - 1)] + [1])        #Generate next row and append it to result.
        return result
