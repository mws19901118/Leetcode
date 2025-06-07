class Solution:
    def clearStars(self, s: str) -> str:
        indexes = {x:[] for x in 'abcdefghijklmnopqrstuvwxyz'}           #Store the indexes of each character in a stack respectively.
        deleted = [False] * len(s)                                       #Mark if the character on currnet index is deleted.
        for i, x in enumerate(s):                                        #Traverse s.
            if x != '*':                                                 #If x is not '*', append its index to corresponding index stack.
                indexes[x].append(i)
            else:                                                        #Otherwise, mark i as deleted first.
                deleted[i] = True
                for y in indexes:                                        #Traverse indexes.
                    if indexes[y]:                                       #If current index stack is not empty, current letter is the smallest.
                        deleted[indexes[y].pop()] = True                 #Pop the last index and mark it as deleted because we always want to only delete the last occurrence.
                        break                                            #Break loop.
        return "".join(x for i, x in enumerate(s) if not deleted[i])     #Join all characters that are not deleted and return.
