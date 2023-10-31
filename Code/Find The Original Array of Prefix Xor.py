class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[i] ^ (pref[i - 1] if i > 0 else 0) for i in range(len(pref))]        #Return the xor of each adjacent number in pref while first number is pref[0].
