class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()                                                                                                      #Sort slots1 in ascending order.
        slots2.sort()                                                                                                      #Sort slots2 in ascending order.
        i, j = 0, 0                                                                                                        #Use 2 pointers to traverse slots1 and slots2 simultanously.
        while i < len(slots1) and j < len(slots2):                                                                         #Find fisrt intersections of time slots that are longer than or equal to duration.
            if slots1[i][1] <= slots2[j][1]:
                if slots2[j][1] >= slots1[i][0] and max(slots1[i][0], slots2[j][0]) + duration <=  slots1[i][1]:
                    return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
                i += 1
            else:
                if slots1[i][1] >= slots2[j][0] and max(slots1[i][0], slots2[j][0]) + duration <=  slots2[j][1]:
                    return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
                j += 1
        return []                                                                                                          #If not found, return empty list.
