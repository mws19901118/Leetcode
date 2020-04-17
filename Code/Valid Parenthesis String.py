class Solution:
    def checkValidString(self, s: str) -> bool:
        lower, upper = 0, 0             #Count the lower bound and upper bound of open '('.
        for x in s:
            if x == '(':                #If current character is '(', increase both lower bound and upper bound.
                lower += 1
                upper += 1
            elif x == ')':              #If current character is ')', decrease both lower bound and upper bound.
                lower -= 1
                upper -= 1
            else:                       #If current character is '*', decrease lower bound and increase upper bound.
                lower -= 1
                upper += 1

            if upper < 0:               #If upper bound is smaller than 0, return false directly.
                return False
            lower = max(lower, 0)       #Lower bound should always be at lease 0.

        return lower == 0               #If final lower bound is 0, the string is valid.
