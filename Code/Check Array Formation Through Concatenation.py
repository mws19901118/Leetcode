class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        indexes = {p[0]: i for i, p in enumerate(pieces)}           #Store the index in pieces for starting number of each piece. 
        i, j = -1, -1                                               #Store the location of current number in pieces.
        for x in arr:                                               #Traverse through arr.
            if i == -1:                                             #If i == -1, it's the start of a piece.
                if x not in indexes:                                #Because numbers are distinct, try to find the index of piece with starting number eqauls current number.
                    return False                                    #If no such piece found, return false.
                i, j = indexes[x], 0                                #Update i to the index and j to 0.
            if x != pieces[i][j]:                                   #If current number does not equal the number in piece, return false.
                return False
            j += 1                                                  #Increase j.
            if j == len(pieces[i]):                                 #If j reaches the end of a piece, set i and j to -1 and -1.
                i, j = -1, -1
        return True                                                 #After traverse, return true.
