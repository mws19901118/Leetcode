class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)               #Count each letter in word1 and word2 respectively.
        for x, y in product(counter1, counter2):                          #Enumerate each distinct possible swap of letters.
            size1, size2 = len(counter1), len(counter2)                   #Get the current distinct charcters in word1 and word2.
            if x != y:                                                    #If x != y, simulate the process of swapping.
                size1 += (y not in counter1) - (counter1[x] == 1)
                size2 += (x not in counter2) - (counter2[y] == 1)
            if size1 == size2:                                            #If sizes are equal, return true.
                return True
        return False                                                      #Return false at the end.
