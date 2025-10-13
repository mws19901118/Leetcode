class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        for x in words:                                            #Traverse words.
            if not result or Counter(result[-1]) != Counter(x):    #Append to result if result is empty or x is not an anagram of result[-1].
                result.append(x)
        return result
