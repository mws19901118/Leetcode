class Solution:
    def removePalindromeSub(self, s: str) -> int:
        steps = ('a' in s) + ('b' in s)         #Because s only contains 'a' and 'b', so steps are at most 2(1 for removing all 'a' and 1 for removing all 'b').
        if steps == 2 and s == s[::-1]:         #If s itself is palindrome, it can be removed in one step.
            steps -= 1
        return steps                            #Return steps.
