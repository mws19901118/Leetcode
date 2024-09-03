class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = "".join([str(ord(x) - ord('a') + 1) for x in s])      #Convert to digits.
        for _ in range(k):                                             #Transform k times.
            digits = str(sum(int(x) for x in digits))
        return int(digits)                                             #Return result as int.
