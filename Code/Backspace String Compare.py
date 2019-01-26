class Solution(object):
    def backspaceEffect(self, text, index):                #Simulate the effect of backspace. Find the index of first non backspace character after having a series of backspace.
        while index >= 0 and text[index] == '#':           #While current character is backspace and the index is valid, start loop.
            backspaceCount = 0                             #Count the number of backspace.
            while index >= 0:
                if text[index] == '#':                     #If current character is backspace, plus one to backspace count.
                    backspaceCount += 1
                else:                                      #Otherwise, it offsets a backspace and the current character is deleted, minus one to backspace count.
                    backspaceCount -= 1
                index -= 1                                 #Move to previous character.
                if backspaceCount == 0:                    #If no more backspace, we find a non backspace character, then break loop.
                    break
        return index                                       #Return the current index.
    
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sIndex = len(S) - 1                               #Index of current character in S.
        tIndex = len(T) - 1                               #Index of current character in T.
        while sIndex >= 0 and tIndex >= 0:                #Because characters won't be affected by previous backspace, we compare from the end to start.
            if S[sIndex] != '#' and T[tIndex] != '#':     #If current character of S and T are both not backspace, compare them.
                if S[sIndex] == T[tIndex]:                #If they are equal, move to previous ones.
                    sIndex -= 1
                    tIndex -= 1
                else:                                     #Otherwise, S and T can't be same.
                    return False
            sIndex = self.backspaceEffect(S, sIndex)      #Simulate the backspace effect on S.
            tIndex = self.backspaceEffect(T, tIndex)      #Simulate the backspace effect on T.
        return sIndex == tIndex                           #If sIndex and tIndex are still same, it means we have go over both entire strings and they are equal.
