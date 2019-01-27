class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        distances = [len(S)] * len(S)                   #Use a list to save distances.
        indexes = []                                    #Store the indexes of C.
        for i, s in enumerate(S):                       #Find all the C in S, set distances of C to 0 and save the indexes of C.
            if s == C:
                distances[i] = 0
                indexes.append(i)
        for i in range(indexes[0]):                     #Handle the distances before first C.
            distances[i] = indexes[0] - i
        
        for i in range(len(indexes) - 1):               #Handle the distances between each C.
            mid = (indexes[i + 1] - indexes[i]) / 2
            for j in range(1, mid + 1):
                distances[indexes[i] + j] = j
                distances[indexes[i + 1] - j] = j
                
        for i in range(1, len(S) - indexes[-1]):        #Handle the distances after last C.
            distances[indexes[-1] + i] = i
            
        return distances
