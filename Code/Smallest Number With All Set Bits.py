class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1    #Left shift 1 the bit length of n then minus 1.
