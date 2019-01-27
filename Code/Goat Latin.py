class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        words = S.split(" ")              #Split S to words.
        for i, w in enumerate(words):
            if w[0] in vowels:            #Covert word starting with vowel.
                w = w + "ma"
            else:                         #Covert word not starting with vowel.
                w = w[1:] + w[0] + "ma"
            w += "a" * (i + 1)            #Append "a"s to the end.
            words[i] = w
        return " ".join(words)            #Join coverted words by space and return.
