class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")  #The furthest point should be replacing all '_' to either 'L' or 'R' to reduce back-and-forth. So, just return the abs difference between 'R' count and 'L' count, then add '_' count.
