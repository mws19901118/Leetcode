class Solution:
    def binaryGap(self, n: int) -> int:
        binary = "{0:b}".format(n)                    #Covert to n binary in string.
        result, last = 0, 0
        for i, x in enumerate(binary):                #Traverse binary string and find the longest distance.
            if x == '1':
                result = max(i - last, result)
                last = i
        return result     
