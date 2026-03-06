class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s      #Cannot have "01" pattern in the string.
