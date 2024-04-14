class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)                                                    #Count each letter in s.
        return Counter([x & 1 for x in count.values()])[1] <= 1               #Cannot have a palindrome permutation if number of odd count is greater than 1.
