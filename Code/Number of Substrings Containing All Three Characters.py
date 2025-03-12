class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_index = {'a': -1, 'b': -1, 'c': -1}                                                    #Initialize the last index of 'a', 'b' and 'c'.
        result = 0                                                                                  #Initialize result.
        for i, x in enumerate(s):                                                                   #Traverse s.
            last_index[x] = i                                                                       #Update last index of x.
            result += all(y > -1 for y in last_index.values()) * (min(last_index.values()) + 1)     #If all 'a', 'b' and 'c' are visited, add the min value of last indexes plus 1 to result; because all substrings starting within s[:min(last_index.values())] and ending at i will have all of 'a', 'b' and 'c' at least once.
        return result
