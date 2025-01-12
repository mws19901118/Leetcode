class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:                                              #If length of s is odd, return false as it will never be valid.
            return False
        locked_left, unlocked = 0, 0                                #Initialize locked '(' and unlocked count.
        for x, y in zip(s, locked):                                 #Traverse s and locked forwards simultaneously.
            if y == "0":                                            #If y is '0', increase unlocked.
                unlocked += 1
            elif x == "(":                                          #If x is '(', increase locked_left.
                locked_left += 1
            elif x == ")":                                          #If x is ')', either locked_left or unlocked should be greater than 0; otherwise it is not matched so return false.
                if locked_left > 0:                                 #If locked_left is greater than 0, use one to match with current ')' so decrease locked_left.
                    locked_left -= 1
                elif unlocked > 0:                                  #Otherwise, if unlocked is greater than 0, use one to match with current ')' so decrease unlocked.
                    unlocked -= 1
                else:
                    return False

        locked_right = 0                                            #Initialize locked '(' from end to start(could be negative).
        for x, y in zip(reversed(s), reversed(locked)):             #Traverse s and locked backwards simultaneously.
            if y == "0":                                            #If y is '0', it is unlocked, we can use it to match one of locked right, so decrease locked_right.
                locked_right -= 1
                unlocked -= 1                                       #Also decrease unlocked, as we only care about unlocked before current character.
            elif x == "(":                                          #If x is '(', it is unlocked right, we increase locked_right.
                locked_right += 1
                locked_left -= 1                                    #Also decrease locked_left, as we only care about locked_left before current character.
            elif x == ")":                                          #If x is ')', we can use it to match with a locked_right in advance, so decrease locked_right.
                locked_right -= 1
            if locked_right > 0:                                    #If locked_right is greater than 0, it cannot be matched, so return false.
                return False
            if not unlocked and not locked_left:                    #If no more unlocked and locked_left, stop traversing.
                break

        return locked_left <= 0                                     #An the end, return if locked_left is not greater than 0.
