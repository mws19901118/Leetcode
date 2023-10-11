class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        days = []                                                          #Store the start and end of blooms of flowers.
        for s, e in flowers:                                               #Traverse flowers.
            days.append((s, 1))                                            #Append s and 1 to days meaning a flower starts bloom at s.
            days.append((e + 1, -1))                                       #Append e and -1 to days meaning a flower ends bloom at e.
        days.sort()                                                        #Sort days.
        sorted_people = sorted([(x, i) for i, x in enumerate(people)])     #Sort people and keep its original index.
        result = [-1] * len(people)                                        #Initialize result for each people.
        count, index = 0, 0                                                #Initialize full bloom flower count and a index to traverse days.
        for x, i in sorted_people:                                         #Traverse sorted people.
            while index < len(days) and days[index][0] <= x:               #Traverse days while index is value and days[index][0] is not greater than x.
                count += days[index][1]                                    #Add days[index][1] to count.
                index += 1
            result[i] = count                                              #Set result[i] to count.
        return result
