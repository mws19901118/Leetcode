class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        opposite = {'N': 'S', 'S': 'N', 'W': 'E', 'E': 'W'}                    #Store opposite directions in a dictionary.
        direction = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}     #Store the movement of each direction.
        result = 0
        for x, y in ['NE', 'NW', 'SW', 'SE']:                                  #Traverse 4 possible directions.
            u, v, r = 0, 0, k                                                  #Initialize coordinate at origin and remaining characters to change.
            for z in s:                                                        #Traverse s.
                if r and (z == opposite[x] or z == opposite[y]):               #If current character is one of the opposite character of current direction and it is still to change, change current character.
                    z = opposite[z]                                            #Change it the opposite.
                    r -= 1                                                     #Decrease r.
                u += direction[z][0]                                           #Move as directed by current direction.
                v += direction[z][1]
                result = max(result, abs(u) + abs(v))                          #Calculate manhattan distance and update result if necessary.
        return result
