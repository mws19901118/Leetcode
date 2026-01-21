class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []                                                      #Same as Construct the Minimum Bitwise Array I.py
        for x in nums:
            if x == 2:
                result.append(-1)
                continue
            b = "{0:b}".format(x)
            index = len(b) - 1
            while index >= 0 and b[index] == '1':
                index -= 1
            y = b[:index + 1] + "0" + "1" * (len(b) - index - 2)
            result.append(int(y, 2))
        return result
