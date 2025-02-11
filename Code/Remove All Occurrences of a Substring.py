class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = ""                                                          #Initialize result.
        for x in s:                                                          #Traverse s.
            result += x                                                      #Append x to result.
            if len(result) >= len(part) and part == result[-len(part):]:     #If the suffix of result has part, remove that suffix.
                result = result[:-len(part)]                
        return result
