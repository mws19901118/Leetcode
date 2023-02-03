class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                                                                    #If there is only one row, we don't have to convert.
            return s
        rows = [[] for _ in range(numRows)]                                                 #Initialize characters at each row.
        segment = (numRows - 1) * 2                                                         #Each segment of zigzag is of (numRows - 1) * 2 length.
        for i, x in enumerate(s):                                                           #Traverse s.
            j = i % segment                                                                 #Find the index of s in current segment.
            rows[j if j < numRows - 1 else (numRows - 1) * 2 - j].append(x)                 #If j < numRows - 1, append s to rows[j], first part of zipzag; otherwise, append s to rows[(numRows - 1) * 2 - j], second part of zigzag.
        return "".join("".join(r) for r in rows)                                            #Join each row then join all rows together.
