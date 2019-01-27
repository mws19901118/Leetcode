class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        i = 0
        while i < len(S):                       #2 pointers.
            j = i
            while j < len(S) and S[i] == S[j]:
                j += 1
            if j - i >= 3:                      #If find large group, add starting index and ending index to result.
                result.append([i, j - 1])
            i = j
        return result
