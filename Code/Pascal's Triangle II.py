class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]                                                            #Initially, the left end is 1.
        for i in range(rowIndex // 2):
            result.append(result[-1] * (rowIndex - i) // (i + 1))               #Generate the binomial coefficient from left to middle.
        for i in range((rowIndex + 1) // 2):
            result.append(result[rowIndex // 2 - i - (rowIndex + 1) % 2])       #Cope the left half reversely to the right half.
        return result
