class Solution:
    def DFS(self, rooms: List[List[int]], current: int, visited: set) -> bool:      #DFS.
        visited.add(current)                                                        #Add current room to visited.
        if len(visited) == len(rooms):                                              #If visited rooms count equals to total number of rooms, return true.
            return True
        for x in rooms[current]:                                                    #For all the keys in current room, if it's room is not visited and can visit all room after DFS from there, return true.
            if x not in visited and self.DFS(rooms, x, visited):
                return True
        return False                                                                #Otherwise cannot visited all room yet, return false.
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return self.DFS(rooms, 0, set())                                            #Do DFS.
