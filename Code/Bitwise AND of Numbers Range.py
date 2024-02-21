class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:                                   #Suppose S is the binary of left and T is the binary of right. Then the answer's binary is the common_prefix(S, T) padding the rest bits with 0.
        k = 0                                                                                  #Count unmatching bits.
        while left != right:                                                                   #While left != right, right shift left and right, update the count of unmatching bits.
            left >>= 1
            right >>= 1
            k += 1
        return right << k                                                                      #Pad 0.
    
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1 if left != right else left     #Recursive version.
