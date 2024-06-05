class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])                          #Initialize common counter to be counter of first word.
        for w in words[1:]:                                 #Traverse rest of words.
            current = Counter(w)                            #Get current count.
            for x in common:                                #Replace count in common if current character has a smaller count in current counter.
                common[x] = min(common[x], current[x])
        return common.elements()                            #Return the elements of common.
