class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS, countT = Counter(s), Counter(t)                                                            #Count each character in s and t.
        return sum(abs(countS[x] - countT[x]) for x in "abcdefghijklmnopqrstuvwxyz") // 2                  #Calculate the total difference between each counter; since one operation will reduce difference by 2, return the half of total difference.
