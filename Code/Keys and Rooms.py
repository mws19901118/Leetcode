class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def DFS(current: int, visited: set) -> bool:                                                                            #DFS.
            visited.add(current)                                                                                                #Add current room to visited.
            return len(visited) == len(rooms) or any(DFS(x, visited) for x in rooms[current] if x not in visited)               #If visited rooms count equals to total number of rooms, return true; otherwise, for all the keys in current room and its room is not visited, return true if either can visit all room after DFS from there.

        return DFS(0, set())                                                                                                    #Start DFS from the first room.
