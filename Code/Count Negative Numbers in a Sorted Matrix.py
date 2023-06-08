class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(len(row) - bisect_right(row, 0, key = lambda x: -x) for row in grid)       #Binary search for the right most place to insert 0, so all the elements on the right of that index is negative. Sum up count in each row.
