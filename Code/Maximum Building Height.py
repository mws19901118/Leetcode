class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = sorted([[1, 0]] + restrictions)                                                                              #Add [1, 0] to restrictions then sort by id.
        if restrictions[-1][0] != n:                                                                                                #If the last id is not in restriction, append [n, n - 1], the max height at n, to restrictions.
            restrictions.append([n, n - 1])
        m = len(restrictions)                                                                                                       #Get the length of restrictions.
        for i in range(1, m):                                                                                                       #Traverse forwards.
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0]))    #Update the practiacal max height of i based on the height of i - 1.
        for i in reversed(range(m - 1)):                                                                                            #Traverse backwards.
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0]))    #Update the practiacal max height of i based on the height of i + 1.
        result = 0
        for i in range(m - 1):                                                                                                      #Traverse from 0 to m - 2.
            highest = ((restrictions[i + 1][0] - restrictions[i][0]) + restrictions[i][1] + restrictions[i + 1][1]) // 2            #Calculate the highest height from restrictions[i] to restrictions[i + 1]. Let's say the turning point is x step from restrictions[i]. Then, restrictions[i][1] + x - ((restrictions[i + 1][0] - restrictions[i][0] - x) <= restrictions[i][1]. So, x <= (restrictions[i + 1][1] - restrictions[i][1] + restrictions[i + 1][0] - restrictions[i][0]) // 2. Now the highest point is h + x <= (restrictions[i + 1][1] + restrictions[i][1] + restrictions[i + 1][0] - restrictions[i][0]) // 2.
            result = max(result, highest)                                                                                           #Update result if necessary.
        return result
