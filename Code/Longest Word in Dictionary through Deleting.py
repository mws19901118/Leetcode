class Solution:
    def canForm(self, s: str, w: str) -> bool:                                                            #Use 2 pointers to check if w is a sub-squence of s.
        i, j = 0, 0
        while i < len(s):
            if j < len(w) and s[i] == w[j]:
                j += 1
            i += 1
        return j == len(w)
    def findLongestWord(self, s: str, d: List[str]) -> str:
        result = ""                                                                                       #Initialize result to be an empty string.
        for w in d:                                                                                       #Traverse all words in d.
            if self.canForm(s, w) and (len(w) > len(result) or (len(w) == len(result) and w < result)):   #If w can be formed from s and w is longer than result or has same length but is lexicographically smaller, update result to be w.
                result = w
        return result
