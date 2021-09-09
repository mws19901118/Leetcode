class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = [x for x in s]                                                            #Split s into letters.
        totalShift = 0                                                                      #Initialize the total shift for current letter.
        for i in reversed(range(len(s))):                                                   #Traverse s and shifts backwards.
            totalShift = (totalShift + shifts[i]) % 26                                      #Update totalShift.
            letters[i] = chr((ord(letters[i]) - ord('a') + totalShift) % 26 + ord('a'))     #Shift current letter.
        return "".join(letters)                                                             #Join letters and return.
