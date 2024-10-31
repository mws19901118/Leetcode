class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()                                                                                  #Sort robot.
        factory.sort(key = lambda x: x[0])                                                            #Sort factory by position.
        factory_positions = []                                                                        #Flatten factory so each factory is duplicated limit times.
        for f in factory:
            factory_positions.extend([f[0]] * f[1])

        result = [[None] * (len(factory_positions) + 1) for _ in range(len(robot) + 1)]               #Cache result.
        def dp(i: int, j: int) -> int:                                                                #DP to calculate the mimimum distance to allocate robot[i:] to factory_positions[j:].
            if result[i][j]:                                                                          #If result[i][j is not none, return result[i][j.
                return result[i][j]
            if i == len(robot):                                                                       #If i reaches the end of robot, no more distance needed, return 0.
                return 0
            if j == len(factory_positions):                                                           #If j reaches the end of factory_positions, cannot allocate more robot, return inf.
                return inf

            assign = abs(robot[i] - factory_positions[j]) + dp(i + 1, j + 1)                          #Allocate robot[i] to factory_positions[j] and keep dp.
            skip = dp(i, j + 1)                                                                       #Skip factory_positions[j] and keep dp.
            result[i][j] = min(assign, skip)                                                          #Set result[i][j] to the minimum of above 2 values.
            return result[i][j]                                                                       #Return result[i][j].

        return dp(0, 0)                                                                               #Return dp(0, 0).
