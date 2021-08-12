class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = defaultdict(list)                                #Group anagrams in defaultdict.
        for word in strs:                                               #Traverse strs.
            anagramsDict["".join(sorted(list(word)))].append(word)      #Split word to letters, then join the sorted letters to get the unique identifier of a group of anagram; append word to corrsponding list by unique identifier.
        return anagramsDict.values()                                    #Return values of anagramsDict.
