class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        count = 0
        for x in shift:                   #Count the total distance shift right.
            if x[0] == 1:
                count += x[1]
            else:
                count -= x[1]
        count %= len(s)                   #Get the modulo because total distance shift should be smaller than length of string. 
        return s[-count:] + s[:-count]    #Perform shift.
