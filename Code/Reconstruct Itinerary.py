class Solution:        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def DFS() -> bool:
            if len(itinerary) == len(tickets) + 1:                        #If the length of itinerary is the length of tickets plus 1, we found a valid itinerary so return True.
                return itinerary
            stop = itinerary[-1]                                          #Get the latest stop.
            for destination in graph[stop]:                               #Traverse its neightbors.
                if count[(stop, destination)] > 0:                        #If there is ticket remaining from stop to destination, keep DFS.
                    itinerary.append(destination)                         #Append destination to itinerary.
                    count[(stop, destination)] -= 1                       #Reduce ticket count.
                    if DFS():                                             #If this direction yield a valid itinerary, return True.
                        return True
                    itinerary.pop()                                       #Otherwise pop itinerary and restore ticket count.
                    count[(stop, destination)] += 1
            return False                                                  #Return false at the end.

        graph, count = defaultdict(list), defaultdict(int)                #Initialize graph and counter for each pair of cities.
        for ticket in tickets:                                            #Build graph and update counter.
            graph[ticket[0]].append(ticket[1])
            count[(ticket[0], ticket[1])] += 1
        for node in graph:                                                #Sort the destinations of each city.
            graph[node].sort()
        itinerary = ["JFK"]                                               #Start itinerary at JFK.
        DFS()                                                             #DFS.
        return itinerary                                                  #Return itinerary.
