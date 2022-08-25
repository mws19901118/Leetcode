class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict, magazineDict = Counter(ransomNote), Counter(magazine)                               #Count each letter in ransom note and magazine.
        return all(x in magazineDict and magazineDict[x] >= ransomNoteDict[x] for x in ransomNoteDict)      #Count of letter in ransom note should be smaller than or equal to its count in magazine.
