class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for x in columnTitle:
            number = number * 26 + ord(x) - ord('A') + 1        #Convert base 26 string to int.
        return number
