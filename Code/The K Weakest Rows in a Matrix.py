class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [index for count, index in sorted([(row.count(1), i) for i, row in enumerate(mat)])[:k]]   #Sort the matrix row indexes by the number of soldiers and then row indexes, then get the first K indexes.
