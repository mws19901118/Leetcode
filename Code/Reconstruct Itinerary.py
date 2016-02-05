class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dict = {}                                 #Use dict to store the available destinations from a certain airport.
        for t in tickets:
            if t[0] not in dict:
                dict[t[0]] = [t[1]]
            else:
                dict[t[0]].append(t[1])
        stack = ['JFK']                           #Use stack to store the path. The initial airport is JFK.
        def DFS(start):                           #DFS from certain airport.
            if len(stack) == len(tickets) + 1:    #If all the tickets are used, return the path.
                return stack
            if start not in dict:                 #If current airport has no available destinations, return to the last level.
                return
            dest = sorted(dict[start])            #Sort available destinations of current airport in lexical order.
            for end in dest:
                dict[start].remove(end)           #Remove each destinations from dict.
                stack.append(end)                 #Append each destinations to stack.
                result = DFS(end)                 #Do DFS.
                if result:                        #If find a possible result, return it.
                    return result
                stack.pop()                       #Pop each destinations from stack.
                dict[start].append(end)           #Add each destination back to dict.
        return DFS('JFK')                         #Start DFS at JFK.
