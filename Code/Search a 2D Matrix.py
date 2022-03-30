class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1
        while start < end:                                                                      #Binary search for the row where target should locate.
            mid = (start + end) // 2
            if matrix[mid][0] > target:                                                         #If matrix[mid][0] > target, target can only be in matrix[:mid].
                end = mid - 1
            elif matrix[mid][-1] < target:                                                      #If matrix[mid][-1] < target, target can only be in matrix[mid + 1:].
                start = mid + 1
            else:                                                                               #Otherwise, target can only be in matrix[mid].
                start, end = mid, mid
        index = bisect_left(matrix[start], target)                                              #Binary search for the left-most index to insert target in matrix[start].
        return index != len(matrix[start]) and matrix[start][index] == target                   #If index is valid and target is at the index, return true; otherwise, return false.
