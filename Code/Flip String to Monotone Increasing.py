class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, flip = 0, 0                       #Count number of '1' and number of flips neede to make traversed part monotone increasing.
        for x in s:                             #Traverse s.
            if x == "1":                        #If x == '1', increase ones.
                ones += 1
            else:                               #Otherwise, the traversed part is not monotone increasing.
                flip = min(ones, flip + 1)      #We have 2 options here: flip all '1' traversed or flip current '0' to '1'. Take the minimum flips.
        return flip                             #Return flip.
