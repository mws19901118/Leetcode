class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count, result = 0, 0      #Just count non-matched parentheses.
        for x in s:
            if x == '(':
                count += 1
            elif count > 0:
                count -= 1
            else:
                result += 1
        result += count
        return result
