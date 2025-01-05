class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        delta = Counter()                                                                #Count the overall shift at each index.
        for x, y, d in shifts:                                                           #Traverse shifts.
            delta[x] += -1 if not d else 1                                               #The start of shift will shift backward if d is 1 and shift forward if d is 0.
            delta[y + 1] += 1 if not d else -1                                           #The next of end of shift will shift forward if d is 1 and shift backward if d is 0.
        result, prefix_shift = [], 0                                                     #Initialize result and prefix shift.
        for i, x in enumerate(s):                                                        #Traverse s.
            prefix_shift = (prefix_shift + delta[i]) % 26                                #Add delta[i] to prefix shift and take modulo by 26 so it is always shift forward within the alphabet.
            result.append(chr((ord(x) - ord('a') + prefix_shift) % 26 + ord('a')))       #Perform the shift for x and append it to result.
        return "".join(result)                                                           #Join result and return.
