class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0                                                                                         #Initialzie 2 pointers.
        intersections = []                                                                                  #Intiialzie intersections.
        while i < len(firstList) and j < len(secondList):                                                   #Traverse while both 2 pointers not reaching the end.
            if firstList[i][1] < secondList[j][1]:                                                          #Handle the case firstList[i][1] < secondList[j][1].
                if firstList[i][1] >= secondList[j][0]:                                                     #If firstList[i][1] >= secondList[j][0], append [max(firstList[i][0], secondList[j][0]), firstList[i][1]] to intersections.
                    intersections.append([max(firstList[i][0], secondList[j][0]), firstList[i][1]])
                i += 1                                                                                      #Move i to next.
            else:                                                                                           #Handle the case firstList[i][1] >= secondList[j][1].
                if secondList[j][1] >= firstList[i][0]:                                                     #If secondList[j][1] >= firstList[i][0], append [max(firstList[i][0], secondList[j][0]), secondList[j][1]] to intersections.
                    intersections.append([max(firstList[i][0], secondList[j][0]), secondList[j][1]])
                j += 1                                                                                      #Move j to next.
        return intersections                                                                                #Return intersections.
