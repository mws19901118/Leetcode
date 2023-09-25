class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts, countt = Counter(s), Counter(t)                 #Count letters in s and t.
        return [x for x in countT if countT[x] - countS[x]][0]  #Return the only letter that has fewer count in countS than in countT.
