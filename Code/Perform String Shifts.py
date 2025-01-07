class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = sum((-y if not x else y) for x, y in shift) % len(s) #Count the total distance shift right and get the modulo because total distance shift should be smaller than length of string. 
        return s[-count:] + s[:-count]                               #Perform shift.
