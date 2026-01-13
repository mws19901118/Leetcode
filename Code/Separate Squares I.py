class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea = sum(l * l for _, _, l in squares)                                      #Calculate total area.
        start, end = min(y for _, y, _ in squares), max(y + l for _, y, l in squares)      #Calculate the min and max y to binary search.
        while end - start > 10 ** -5:                                                      #Binary search while start and end are not same.
            mid = (start + end) / 2                                                        #Calculate mid.
            area = sum(l * max(0, min(l, mid - y)) for _, y, l in squares)                 #Calculate the area below mid.
            if area >= totalArea / 2:                                                      #If the area below mid is greater than or equal to half of total area, set end to mid.
                end = mid
            else:                                                                          #Otherwise, set start to mid.
                start = mid
        return start                                                                       #Return start.
