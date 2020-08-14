class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)                          #Count each letter.
        length, single = 0, 0
        for c in count:
            length += count[c] - count[c] % 2       #For each letter c, if count[c] is even, it can contribute count[c] to palindrome; if count[c] is odd, it can contribute count[c] - 1 to palindrome.
            single = max(single, count[c] % 2)      #If there is letter whose count is odd, longest palindrome can add one more single letter.
        return length + single
