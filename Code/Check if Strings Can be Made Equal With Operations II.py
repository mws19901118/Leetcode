class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter([x for i, x in enumerate(s1) if i & 1]) == Counter([x for i, x in enumerate(s2) if i & 1]) and Counter([x for i, x in enumerate(s1) if not i & 1]) == Counter([x for i, x in enumerate(s2) if not i & 1])   #Same as Check if Strings Can be Made Equal With Operations I.py
