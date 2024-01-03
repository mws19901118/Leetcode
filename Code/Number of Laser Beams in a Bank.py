class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lastRowCount, result = 0, 0                              #Store the security devices count in last row that has security devices also initialize result.
        for r in bank:                                           #Traverse each row.
            currRowCount = r.count("1")                          #Count the security devices in current row.
            if currRowCount > 0:                                 #If the count is greater than 0, add lastRowCount * currRowCount to result and replace lastRowCount with currRowCount.
                result += lastRowCount * currRowCount
                lastRowCount = currRowCount
        return result
