class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)        #Count each character.
        for i, x in enumerate(s):             #Traverse from begining, if count of a character is 1, return its index.
            if count[x] == 1:
                return i     
        return -1                             #If not found, return -1.
