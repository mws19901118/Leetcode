class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]                                  #Initially, there is no '1' in 0.
        i = 1                                         #Iterate every power of 2, starting from 1.
        while i <= num:
            for j in range(i, min(2 * i, num + 1)):   #For every number j from i to min(2 * i, num + 1), result[j] = result[j - i] + 1, becase of the '1' on the most significant bit.
                result.append(result[j - i] + 1)
            i *= 2                                    #Go to the next power of 2.
        return result
