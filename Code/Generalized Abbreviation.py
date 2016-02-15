class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        l = len(word)                           #Get the length of word.
        n = 2 ** l                              #Each character has 2 state: indicated by itself or indicated by digit. So total number of state is 2^l.
        result = []
        for i in range(n):
            abbr = ""
            temp = i
            count = 0                           #Count consecutive characters indicated by digit.
            for j in range(l):
                if temp % 2 == 0:               #If temp is even, it's indicated by digit.
                    count += 1
                else:                           #Otherwise it's indicated by itself.
                    if count != 0:              #If count is not 0, add count to abbreviation and reset count.
                        abbr += str(count)
                        count = 0               #Add it self to abbareviation.
                    abbr += word[j]
                temp = temp >> 1                #Shift temp.
            if count != 0:                      #If count is not 0, add count to abbreviation and reset count.
                abbr += str(count)
            result.append(abbr)
        return result
