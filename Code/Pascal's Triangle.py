class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = [[1]]                                               #Initialize first row.
        for i in range(1, numRows):                             #Generate remaining row.
            p.append([1])                                       #Append the leftmost 1.
            for j in range(1, i):                               #Generate numbers in the middle.
                p[-1].append(p[i - 1][j - 1] + p[i - 1][j])
            p[-1].append(1)                                     #Append the rightmost 1.
        return p
