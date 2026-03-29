class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter([x for i, x in enumerate(s1) if i & 1]) == Counter([x for i, x in enumerate(s2) if i & 1]) and Counter([x for i, x in enumerate(s1) if not i & 1]) == Counter([x for i, x in enumerate(s2) if not i & 1])  #Return true if the characters on odd indexes and even indexes are the same group in s1 and s2 respectively.
