class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return sum(int(x) + int(y) if not int(z) else 1 - (int(x) | int(y))for x, y, z in zip(format(a, '031b'), format(b, '031b'), format(c, '031b')))            #Convert a, b and c to 31 bits binary with leading 0. Then traverse simultaneously and calculate flips based on bit value.
