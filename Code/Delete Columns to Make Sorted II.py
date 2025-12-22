class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        isSorted = [False] * (len(strs) - 1)                                                            #Store if a row is smaller than next row; initially all false because we know nothing yet.
        for column in zip(*strs):                                                                       #Traverse each column.
            if any(not isSorted[i] and column[i] > column[i + 1] for i in range(len(strs) - 1)):        #If there is any row not already smaller than next row and current column is greater than the same column of next row, we have to remove the whole column.
                result += 1                                                                             #Thus increase result and continue.
                continue
            for i in range(len(strs) - 1):                                                              #Traverse this column again.
                if column[i] < column[i + 1]:                                                           #For the rows whose current column is smaller than the same column of next row, mark the row as already sorted.
                    isSorted[i] = True
        return result
