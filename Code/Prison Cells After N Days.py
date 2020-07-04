from functools import reduce
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        days = {}                                                     #Store the days of the first appearance of each cells pattern.
        seen = []                                                     #Store all seen patterns in each day.
        count = 0                                                     #Count days.
        num = reduce(lambda a, b : (a << 1) + b, cells)               #Because each cells pattern is 8 binaries, it can be converted to a integer.
        while num not in days:                                        #While num is not seen in days, we haven't find a cycle.
            days[num] = count                                         #Add current pattern's integer to days.
            seen.append(cells)                                        #Also add current pattern to seen.
            count += 1                                                #Go to next day
            newCells = [0]                                            #Create the pattern for next day.
            for i in range(1, 7):                                     #Iterate between 1 to 6 cause the cells on both end will always be 0.
                newCells.append(1 - cells[i - 1] ^ cells[i + 1])      #Update cells value based on previous pattern.
            newCells.append(0)
            cells = newCells                                          
            if count == N:                                            #If we already reaches day N, return current cells.
                return cells
            num = reduce(lambda a, b : (a << 1) + b, cells)           #Convert current pattern to integer.
        cycle = count - days[num]                                     #Between the day when current pattern is first seen and current day, patterns form a cycle.
        remain = days[num]                                            #And the rest of patterns are seen before entering cycle.
        return seen[(N - remain) % cycle + remain]                    #Caculate the position of day N in cycle plus rest of days and then return.
