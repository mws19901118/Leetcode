class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result, altitude = 0, 0                 #Initialize result and altitude.
        for x in gain:                          #Traverse gain.
            altitude += x                       #Calculate current altitude. 
            result = max(result, altitude)      #Update result if necessary.
        return result
