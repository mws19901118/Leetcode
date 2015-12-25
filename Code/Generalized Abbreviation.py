class Solution(object):
    def backtrack(self, word, dict):
        if word == "":                                    #If word is empty, return [""]. 
            return [""]
        if word in dict:                                  #If word is already in dict, return dict[word].
            return dict[word]
        result = set()                                    #Use a set to store current result and rule out duplicates.
        for i in range(len(word)):                        #Traverse through every character of word.
            l = self.backtrack(word[:i], dict)            #Find all the generalized abbreviations of left part.
            r = self.backtrack(word[i + 1:], dict)        #Find all the generalized abbreviations of right part.
            for j in l:
                for k in r:
                    result.add(j + word[i] + k)           #For every abbreviation of left part and every abbreviation of right part, merge them together with current character.
        result.add(str(len(word)))                        #Add length of current word as a generalized abbreviation.
        abbr = list(result)                               #Convert from set to list.
        dict[word] = abbr                                 #Store current result in dict.
        return abbr                                       #Return current result.
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        dict = {}                                         #Use dict to buffer intermediate result.
        return self.backtrack(word, dict)                 #Backtrack.
