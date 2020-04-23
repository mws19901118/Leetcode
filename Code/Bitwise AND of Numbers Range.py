class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:                           #Suppose S is the bit string of n and T is the bit string of m. Then the answer's bit string is the common_prefix(S, T) padding the rest bits with 0.
        k = 0                                                                   #Count unmatching bits.
        while n != m:                                                           #While n != m, right shift m and n, update the count of unmatching bits.
            n >>= 1
            m >>= 1
            k += 1
        return n << k                                                           #Pad 0.
    
    def rangeBitwiseAnd(self, m: int, n: int) -> int:                           #Recursive version.
        return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if m != n else m       
