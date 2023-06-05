class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        vector = (coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1])                                     #Calculate the vector from first point to second point.
        return all((c[0] - coordinates[0][0]) * vector[1] == (c[1] - coordinates[0][1]) * vector[0] for c in coordinates[2:])       #Each vector from the first point to any other point should be parallel with the above vector.
