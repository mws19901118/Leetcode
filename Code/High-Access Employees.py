class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        accessTimeByEmployee = defaultdict(list)                                                              #Group access times by employee.
        for x, t in access_times:
            accessTimeByEmployee[x].append(t)
        result = []
        for x in accessTimeByEmployee:                                                                        #Traverse each employee.
            accessTimeByEmployee[x].sort()                                                                    #Sort access time.
            for i in range(2, len(accessTimeByEmployee[x])):                                                  #If employee accesses more than twice and any access and its 2 previous accesses locate in one hour window, add employee to result and continue.
                hour, time = int(accessTimeByEmployee[x][i][:2]), int(accessTimeByEmployee[x][i][2:])
                count = 0
                for p in accessTimeByEmployee[x][i - 2:i]:
                    pHour, pTime = int(p[:2]), int(p[2:])
                    if (pHour == hour - 1 and pTime > time) or (pHour == hour and pTime <= time):
                        count += 1
                if count == 2:
                    result.append(x)
                    break
        return result
