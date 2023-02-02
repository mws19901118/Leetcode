class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderTable = {x: i for i, x in enumerate(order)}                                                #Convert order to a hash table.
        def inOrder(a: str, b: str) -> bool:
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:                                           #Find the first difference character between a and b.
                i += 1
            return i == len(a) or (i != len(b) and orderTable[a[i]] < orderTable[b[i]])                 #If a < b then either i reaches the end of a or (i hasn't reach the end of b and the order of a[i] is smaller than the order of b[i]).

        return all(inOrder(words[i], words[i + 1]) for i in range(len(words) - 1))                      #Return all word is lexicographicaly smalled than or equal to next word.
