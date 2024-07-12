class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def getPoints(string: str, aFirst: bool) -> int:                                #Calculate the points to perform operations on string with proritizing ab over ba or vice versa.
            first, second = ('a', 'b') if aFirst else ('b', 'a')                        #Get the first and second letter based on the priority flag.
            highPoint, lowPoint = (x, y) if aFirst else (y, x)                          #Get the points of each operation based on priority flag.
            firstCount, secondCount, points = 0, 0, 0                                   #Count first letter, second letter and total points. 
            for c in string:                                                            #Traverse string.
                if c == first:                                                          #If current letter is first, increase firstCount.
                    firstCount += 1
                elif firstCount:                                                        #If current letter is second but we have first letter, add highPoint to points and decrease firstCount to perform the high priority opeartion
                    points += highPoint
                    firstCount -= 1
                else:                                                                   #Otherwise, increase secondCount.
                    secondCount += 1
            return points + min(firstCount, secondCount) * lowPoint                     #Perform low priority operation as many as possible on remaining letters, add to points and return.

        i, count = 0, 0
        while i < len(s):                                                               #Traverse s.
            if s[i] not in ['a', 'b']:                                                  #If current letter is neither a nor b, move to next.
                i += 1
                continue
            j = i
            while j < len(s) and s[j] in ['a', 'b']:                                    #Find the substring formed by consecutive a or b.
                j += 1
            count += max(getPoints(s[i:j], True), getPoints(s[i:j], False))             #Try get points on the substring with 2 types of priority respectively and add the max of 2 to count.
            i = j
        return count
