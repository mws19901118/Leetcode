class Solution:
    def numberOfWays(self, corridor: str) -> int:
        total = corridor.count('S')                                        #Count seats.
        if total & 1 or not total:                                         #If number of seats is 0 or odd, return 1 as there is no valid way to divide the corridor.
            return 0
        division = 10 ** 9 + 7                                             #Initialize division.
        i, count, result = 0, 0, 1                                         #Initialize pointer, running count of seat and result.
        while count < total - 1:                                           #Traverse while not entering the last section.
            if corridor[i] == 'S':                                         #Increase count if corridor[i] is seat.
                count += 1
            if corridor[i] == 'P' and count > 0 and not count & 1:         #Find the number of plants between 2 sections.
                j = i + 1
                while j < len(corridor) and corridor[j] == 'P':
                    j += 1
                result = result * (j - i + 1) % division                   #There are j - i + 1 ways to divide plants between 2 sections.
                i = j
            else:
                i += 1
        return result
