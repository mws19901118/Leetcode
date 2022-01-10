class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))                                                                                        #Get the max length of a and b.
        a, b = a.zfill(length), b.zfill(length)                                                                             #Fill a and b to max length.
        carry = 0                                                                                                           #Initialize carry.
        result = []                                                                                                         #Initialize result.
        bits = {'0': 0, '1': 1}
        for i in range(length - 1, -1, -1):                                                                                 #Traverse backwards and calculate result.
            currentBit, carry = (bits[a[i]] + bits[b[i]] + carry) % 2, (bits[a[i]] + bits[b[i]] + carry) // 2
            result.append(str(currentBit))
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])                                                                                        #Reverse result and join it together.
