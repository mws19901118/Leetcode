class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k = k + 1                                                #Increment k to account for 1-based indexing.
        biinary = format(k, 'b')[1:]                             #Convert k to a binary string and ignore the 1 on most significant big.
        result = biinary.replace("0", "4").replace("1", "7")     #Replace '0' with '4' and '1' with '7' in the binary string.
        return result
