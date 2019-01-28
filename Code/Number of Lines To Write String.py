class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1                                           #Count lines.
        length = 0                                          #Store the length of current line.
        for s in S:
            if length + widths[ord(s) - ord('a')] <= 100:   #If current line length plus current character width is not larger than 100, write the character in this line.
                length += widths[ord(s) - ord('a')]
            else:                                           #Otherwise, write in a new line.
                lines += 1
                length = widths[ord(s) - ord('a')]
        return [lines, length]
