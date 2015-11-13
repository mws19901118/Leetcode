class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}                                   #Use a dict to store the last appeareance index of a character.
        l = len(s)
        maxl = 0                                    #Record the max length.
        i = 0                                       #Record the starting index of current substring.
        j = 0                                       #Record the ending index of current substring.
        while j < l:
            if s[j] in dict or len(dict) < 2:       #If the length of dict is smaller than 2 or current character is already in dict, add it and the index to dict.
                dict[s[j]] = j
                if j - i + 1 > maxl:                #Update maxl if necessary.
                    maxl = j - i + 1
            else:                                   #Maintain a dict whose length is 2 when encountering a new character.
                lastappearance = l
                for k in dict.keys():               #Find the smaller index of the last appearance of the 2 characters. The characters on and before that index no longer belong to current substring.
                    if dict[k] < lastappearance:
                        lastappearance = dict[k]
                del dict[s[lastappearance]]         #Remove that character from dict.
                i = lastappearance + 1              #Update the starting index.
                dict[s[j]] = j                      #Add the new character and its index to dict.
            j += 1
        return maxl
