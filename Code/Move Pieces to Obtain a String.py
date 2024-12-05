class Solution:
    def canChange(self, start: str, target: str) -> bool:
        lInTarget, rInStart = 0, 0              #Initialize the L in target and R in start that are unmatched so far.
        for x, y in zip(start, target):         #Traverse start and target simultaneously.
            if x == 'L':                        #Scenario 1 for x is L.
                if y == 'L':                    #If y is 'L' as well, there shouldn't be any unmatched R in start, because they cannot be moved pass current L.
                    if rInStart:
                        return False
                elif y == 'R':                  #If y is 'R', directly return false because no R on the left of start can be moved here.
                    return False
                else:                           #If y is '_', there should be at least 1 unmatched L in target, because this L has to move to there.
                    if not lInTarget:
                        return False
                    lInTarget -= 1             #Decrease lInTarget.
            elif x == 'R':                     #Scenario 2 for x is R.
                if lInTarget:                  #There shouldn't be any unmatched L in target, because L in start behind this R cannot be moved before current R.
                    return False
                if y == 'L':                   #If y is 'L', directly return false because no L on the right of start can be moved here.
                    return False
                elif y == '_':                 #If y is '_', increase rInStart.
                    rInStart += 1
            else:                              #Scenario 3 for x is _.
                if y == 'L':                   #If y is 'L', there shouldn't be any unmatched R in start, because they cannot be moved pass current L..
                    if rInStart:
                        return False
                    lInTarget += 1             #Increase lInTarget.
                elif y == 'R':                 #If y is 'R', there should be at least 1 unmatched R in start, because that R has to move here.
                    if not rInStart:
                        return False
                    rInStart -= 1              #Decrease rInStart.
        return not lInTarget and not rInStart  #At the end, there shouldn't be any unmatched L or R left.
