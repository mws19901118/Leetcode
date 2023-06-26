class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        division = 10 ** 9 + 7                                                                    #Initialize division.
        startLocation, finishLocation = locations[start], locations[finish]                       #Store the actual start location and finish location.
        locations.sort()                                                                          #Sort locations.
        indexDict = {x: i for i, x in enumerate(locations)}                                       #Store indexes by location.
        newStart, newFinish = indexDict[startLocation], indexDict[finishLocation]                 #Get the new index in sorted locations for start and finish.

        @cache                                                                                    #Cache result.
        def DFS(index: int, fuel: int):                                                           #DFS to calculate the total numbers of routes from current location with given fuel.
            count = int(newFinish == index)                                                       #If current location is finish location, initialize count with 1; otherwise with 0.
            i = index - 1                                                                         #Scan to the left to find all valid location for next step.
            while i >= 0 and fuel - (locations[index] - locations[i]) >= 0:
                count += DFS(i, fuel - (locations[index] - locations[i]))                         #Add all DFS result to count.
                i -= 1
            i = index + 1                                                                         #Scan to the right to find all valid location for next step.
            while i < len(locations) and fuel - (locations[i] - locations[index]) >= 0:
                count += DFS(i, fuel - (locations[i] - locations[index]))                         #Add all DFS result to count.
                i += 1
            return count % division                                                               #Return count after taking modulo.
            
        return DFS(newStart, fuel)                                                                #Return DFS(newStart, fuel).
