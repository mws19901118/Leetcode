class Solution:
    def numberOfWays(self, corridor: str) -> int:
        total = corridor.count('S')                                        #Count seats.
        if total & 1 or not total:                                         #If number of seats is 0 or odd, return 1 as there is no valid way to divide the corridor.
            return 0
        division = 10 ** 9 + 7                                             #Initialize division.
        index, result = -1, 1                                              #Initialize last index of seat and result.
        for i, x in enumerate(corridor):                                   #Traverse corridor.
            if x == 'P':                                                   #If current position is plant, skip.
                continue
            if index != -1 and not total & 1:                              #If index is not -1 and total is even now, we can insert a divider any place between index and i.
                result = (result * (i - index)) % division
            index = i                                                      #Update index.
            total -= 1                                                     #Decrease total.
        return result
