class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = defaultdict(int)                                    #Store the occurrences.
        h = 0                                                       #Maintain current h-index.
        buffer = 0                                                  #Record the number of citations which is larger than current h-index.
        for c in citations:                                         #Traverse citations.
            if c > h:                                               #Only consider citations which are larger than current h-index, because citations which are smaller than or equal to current h-index have no impact on h-index.
                buffer += 1                                         #Increase buffer by 1.
                if c <= len(citations):                             #If current citation can be a candiate of h-index, update its occuerrence.
                    count[c] += 1
                if buffer > h:                                      #If buffer is larger than current h-index, increase h-index by 1.
                    h += 1
                    buffer -= count[h]                              #Decrease buffer by the number of occurrence of current h-index.
        return h
