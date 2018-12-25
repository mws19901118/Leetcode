class Solution:
    def inOrder(self, a, b, orderTable):                    #Determine if a is lexicographicaly smalled than or equal to b in orderTable.
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:   #Find the first difference character between a and b.
            i += 1
        if i == len(a):                                     #If it reaches the end of a, meaning a is a prefix of b, then a is smalled than or equal to b.
            return True
        if i == len(b):                                     #If it reaches the end of b, meaning b is a prefix ofab, then a is not smalled than or equal to b.
            return False
        return orderTable[a[i]] < orderTable[b[i]]          #Return if the order of a[i] is smaller than the order of b[i].
    
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderTable = {}
        for i, c in enumerate(order):
            orderTable[c] = i                               #Convert order to a hash table.
        lastWord = ""                                       #A holder for the first comparison.
        for w in words:
            if self.inOrder(lastWord, w, orderTable):       #If current last word is lexicographicaly smalled than or equal to current word, update last word to be current word.
                lastWord = w
            else:                                           #Otherwise, words is not sorted, return false.
                return False
        return True
