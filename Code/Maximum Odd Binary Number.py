class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)                                                #Count '0' and '1' in s.
        return '1' * (count["1"] - 1) + '0' * count['0'] + '1'            #Put 1 '1' on last bit, the rest of '1's in the front then all '0's in the middle.
