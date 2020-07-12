class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, 'b').zfill(32)[::-1], 2)  #Convert int to binary, fill leading 0 to 32 bits, reverse string and convert back to integer.
