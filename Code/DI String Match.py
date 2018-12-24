class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low, high = 0, len(S)         #Low is the smallest available number, while high is the largest available number.
        result = []
        for x in S:
            if x == 'I':              #If current character in S is 'I', current number should be as small as possible so next number is always larger than it.
                result.append(low)
                low += 1
            else:                     #If current character in S is 'D', current number should be as large as possible so next number is always smaller than it.
                result.append(high)
                high -= 1
        result.append(low)            #Add the last available number to result.
        return result      
