class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:                                                #Traverse nums.
            if x == 2:                                                #If x is 2, directly append -1 because it cannot be the result of any y OR (y + 1).
                result.append(-1)
                continue
            b = "{0:b}".format(x)                                     #Convert x to binary string.
            index = len(b) - 1
            while index >= 0 and b[index] == '1':                     #Find the rightmost bit that is not 1.
                index -= 1
            y = b[:index + 1] + "0" + "1" * (len(b) - index - 2)      #Keep b[:index + 1] as the prefix, then add a "0", next shift b[:index + 1] right 1 bit to get the y.
            result.append(int(y, 2))                                  #Convert y from binary string to integer then append to result.
        return result
