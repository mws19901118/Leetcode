class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts, countt = Counter(s), Counter(t)                 #Count letters in s and t.
        for c in countt:                                        #If any letter is only in countt or its count in s is smaller than its count in t, return that letter.
            if c not in counts or countt[c] > counts[c]:
                return c
