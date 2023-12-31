class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        fistIndex = {}                                            #Store the first index of each character.
        for i, x in enumerate(s):                                 #Traverse s.
            if x in fistIndex:                                    #If x is seen before, get the substring length between current x and first x and update result if necessary.
                result = max(result, i - fistIndex[x] - 1)
            else:                                                 #Otherwise, store the index of x.
                fistIndex[x] = i
        return result
