class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        turn = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}            #Use a dictionary to store the clockwise turns.
        m, n = len(room), len(room[0])                                                         #Get the dimensions.
        x, y, u, v = 0, 0, 0, 1                                                                #Initialize position and direction.
        cleaned, visited = set([(0, 0)]), set()                                                #Use a set to store cleaned spaces; also use a set to store the turning point with direction.
        while (x, y, u, v) not in visited:                                                     #Iterate while not turned at current position with same direction.
            visited.add((x, y, u, v))                                                          #Mark current position and direction as visited.
            i, j = x, y
            while 0 <= i + u < m and 0 <= j + v < n and not room[i + u][j + v]:                #Moving forward until reaches an edge or object.
                i += u
                j += v
                cleaned.add((i, j))                                                            #Clean current space.
            x, y = i, j                                                                        #Update position.
            u, v = turn[(u, v)]                                                                #Update direction.
        return len(cleaned)                                                                    #Return the length of cleansd.
