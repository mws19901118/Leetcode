class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        dict = {}                                   #Store the occurrences.
        for i in range(len(citations) + 1):         #The possible value of h-index is from 0 to n.
            dict[i] = 0
        h = 0                                       #Maintain current h-index.
        buffer = 0                                  #Record the number of citations which is larger than current h-index.
        for i in range(len(citations)):             #Take the citations as a stream,
            if citations[i] > h:                    #Only consider citations which are larger than current h-index, because citations which are smaller than or equal to current h-index have no impact on h-index.
                buffer += 1                         #Increase buffer by 1.
                if citations[i] <= len(citations):  #If current citation can be a candiate of h-index, update its occuerrence.
                    dict[citations[i]] += 1
                if buffer > h:                      #If buffer is larger than current h-index, increase h-index by 1.
                    h += 1
                    buffer -= dict[h]               #Decrease buffer by the number of occurrence of current h-index.
        return h
