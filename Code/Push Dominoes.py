class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = ['L'] + list(dominoes) + ['R']            #Convert dominoes to list with default left push at left end and default right push at the right end. 
        i = 0                                         #Initialize pointer i.
        while i < len(d) - 1:                         #Traverse d.
            j = i + 1                                 #Initialize pointer j as i + 1.
            while j < len(d) - 1 and d[j] == '.':     #While j == '.', move j to next. 
                j += 1
            if d[i] == d[j]:                          #If the pushes at d[i] and d[j] are same, then set d[i + 1:j] to d[i].
                for k in range(i + 1, j):
                    d[k] = d[i]
            elif d[i] == 'R' and d[j] == 'L':         #If d[i] is 'R' and d[j] is 'L', the pushes will meet at middle.
                span = (j - i - 1) // 2               #Calculate the span from either i or j to the middle.
                for k in range(1, span + 1):          #Set the left span to 'R' and right span to 'L'.
                    d[i + k] = 'R'
                    d[j - k] = 'L'
            i = j                                     #Move i to j.
        return "".join(d[1:-1])                       #Join d[1:-1] and return(Ignore default pushes at both end).
