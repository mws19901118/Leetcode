class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)                            #Initialize ans with n + 1 zeros.
        mask = 0                                       #Use this mask to take all bits except the mostsignificant bit; initially it's 0.
        for i in range(1, n + 1):                      #Traverse from 1 to n.
            ans[i] = ans[i & mask] + 1                 #The most significant bit of i is 1, so add the count of 1s in the rest then plus 1.
            if i & mask == mask:                       #If the rest is same as mask, it's time to move to a longer binary.
                mask = mask << 1 | 1                   #So we need to update mask as well, shift left 1 bit and or witth 1.
        return ans
