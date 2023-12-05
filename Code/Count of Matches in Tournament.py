class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:                #Simulate tournament while n is greater than 1.
            count += n >> 1         #Play n // 2 matches.
            n = n // 2 + n % 2      #There are n // 2 + n % 2 teams left.
        return count
