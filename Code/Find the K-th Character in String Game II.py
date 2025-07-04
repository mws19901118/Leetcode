class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        result = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            result += operations[t]              #Similar with Find the K-th Character in String Game I, just only increase result when the corresponding operations is 1.
        return chr(ord("a") + result % 26)       #Also take modulo at the end.
