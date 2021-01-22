class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)                                 #Count the letters in each string.
        if counter1.keys() != counter2.keys():                                              #Because Operation 1 allows us to freely reorder the string, so close strings must consist of same set of letters.
            return False
        counter1, counter2 = Counter(counter1.values()), Counter(counter2.values())         #Now, count the count of letters in each string.
        if counter1 != counter2:                                                            #Because Operation 2 allows us to freely reassign the letters' frequencies, so the count of count must be same.
            return False
        return True                                                                         #Return true finally.
