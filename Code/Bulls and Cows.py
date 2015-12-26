class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        l = len(secret)
        filtered = ""                             #Store guess string after filtered all bulls.
        dict = {}                                 #Store the number of occurrence of characters of secret except for bulls.
        bull = 0
        cow = 0
        for i in range(l):
            if secret[i] == guess[i]:             #Calculate bulls.
                bull += 1
            else:
                if secret[i] not in dict:         #Update dict.
                    dict[secret[i]] = 1
                else:
                    dict[secret[i]] += 1
                filtered += guess[i]              #Update filtered.
        for c in filtered:                        #For every characters in filtered, check if it is in dict.
            if c in dict:
                cow += 1
                dict[c] -= 1
                if dict[c] == 0:                  #Remove current character from dict if its occurrence is 0.
                    del dict[c]
        return str(bull) + 'A' + str(cow) + 'B'
