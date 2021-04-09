class Solution:
    def inOrder(self, a: str, b: str, orderTable: dict) -> bool:                                        #Determine if a is lexicographicaly smalled than or equal to b in orderTable.
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:                                               #Find the first difference character between a and b.
            i += 1
        if i == len(a):                                                                                 #If it reaches the end of a, meaning a is a prefix of b, then a is smalled than or equal to b.
            return True
        if i == len(b):                                                                                 #If it reaches the end of b, meaning b is a prefix ofab, then a is not smalled than or equal to b.
            return False
        return orderTable[a[i]] < orderTable[b[i]]                                                      #Return if the order of a[i] is smaller than the order of b[i].
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderTable = {x: i for i, x in enumerate(order)}                                                #Convert order to a hash table.
        return all(self.inOrder(words[i], words[i + 1], orderTable) for i in range(len(words) - 1))     #Return all word is lexicographicaly smalled than or equal to next word.
