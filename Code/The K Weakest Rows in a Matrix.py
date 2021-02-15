class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [sorted([(row.count(1), i) for i, row in enumerate(mat)])[i][1] for i in range(k)]   #Sort the matrix row indexes by the number of soldiers and then row indexes, then get the first K indexes.
