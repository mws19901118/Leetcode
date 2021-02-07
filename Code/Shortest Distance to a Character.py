class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        distances = [-1] * len(s)                                               #Use a list to save distances.
        indexes = [i for i, x in enumerate(s) if x == c]                        #Get the indexes of c.
        j = 0                                                                   #Store the index of first c in front of current charracter in indexes.
        for i, x in enumerate(s):                                               #Traverse s.
            if x == c:                                                          #If x is c, set its distance to 0 and move j to next and continue.
                distances[i] = 0
                j += 1
                continue
            if j == 0:                                                          #Handle the distances before first c.
                distances[i] = indexes[j] - i
            elif j >= len(indexes):                                             #Handle the distances after last c.
                distances[i] = i - indexes[j - 1]
            else:                                                               #Handle other distances, which is the smaller of the distances to the c in front of it and the c behind it.
                distances[i] = min(indexes[j] - i, i - indexes[j - 1])
        return distances
