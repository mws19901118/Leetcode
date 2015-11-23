class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrdict = {}                                                                  #Use a dict to count the number of same abbreviation.
        self.origdict = {}                                                                  #Use a dict to rule out duplicate of original words.
        for x in dictionary:
            if len(x) <= 1:                                                                 #If the length of word is not larger than 1, its abbreviation is itself.
                n = x
            else:                                                                           #Otherwise get the abbreviation as decribed.
                n = x[0] + str(len(x) - 2) + x[-1]
            if x not in self.origdict:                                                      #If this is the 1st time word appears, add the count of abbreviation.
                if n not in self.abbrdict:
                    self.abbrdict[n] = 1
                else:
                    self.abbrdict[n] += 1
              self.origdict[x] = True                                                       #Set it as appeared.
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            n = word
        else:
            n = word[0] + str(len(word) - 2) + word[-1]                                     #Get the abbrviation.
        if n not in self.abbrdict or (self.abbrdict[n] == 1 and word in self.origdict):     #If it is not in abbrdict or the abbrevation count is 1 and the word has appeared in dictionary, return true.
            return True
        else:                                                                               #Otherwise, return false.
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
