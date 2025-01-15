class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1Binary, num2Binary = "{0:b}".format(num1), "{0:b}".format(num2)      #Convert num1 and num2 to binary string.
        num2SetBit = num2Binary.count('1')                                       #Calculate the set bit for num2.
        result = []                                                              #Initialize result.
        for i, x in enumerate(num1Binary):                                       #Traverse num1Binary.
            result.append(x if num2SetBit else '0')                              #If num2SetBit is not 0, append x to result to make the XOR at current bit 0; otherwise, append '0' because no more available '1' to use.
            num2SetBit -= int(x == '1' and num2SetBit > 0)                       #Decrease num2SetBit if x is '1' and num2SetBit is greater than 0 to update remaining num2SetBit.
        if num2SetBit:                                                           #If there are still num2SetBit left, flip '0' to '1' from least significant bit to most signification bit.
            for i in reversed(range(len(num1Binary))):                           #Traverse num1Binary backwards.
                if num1Binary[i] == '0':                                         #If current bit is '0', flip its corresponding result to '1' and decrease num2SetBit.
                    result[i] = '1'
                    num2SetBit -= 1
                if not num2SetBit:                                               #Jump out of loop if num2SetBit reaches 0.
                    break
        if num2SetBit:                                                           #If there are still num2SetBit left, add all of them in front of the most significant bit.
            result.insert(0, '1' * num2SetBit)
        return int("".join(result), 2)                                           #Join result and convert to integer then return.
