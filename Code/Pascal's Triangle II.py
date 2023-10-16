class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]                                                            #Initially, the left end is 1.
        or i in range(rowIndex):                                                #Generate the binomial coefficient from left to right.
            result.append(result[-1] * (rowIndex - i) // (i + 1))
        return result
