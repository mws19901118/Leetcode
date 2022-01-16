class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lastPerson = -1                                                             #Initialize the index of last person.
        distanceToLeft, maxDistance = 0, 0                                          #Initialize the distance from first person to left and the max distance to closest person if sitting between 2 people.
        for i, x in enumerate(seats):                                               #Traverse seat.
            if not x:                                                               #If current seat has no person, continue.
                continue
            if lastPerson == -1:                                                    #If this is the first person, update distanceToLeft.
                distanceToLeft = i
            else:                                                                   #Otherwise, update maxDistance.
                maxDistance = max(maxDistance, (i - lastPerson) // 2)
            lastPerson = i                                                          #Update the index of last person.
        return max(maxDistance, distanceToLeft, len(seats) - 1 - lastPerson)        #Return the max distance of sitting between 2 peoples, on the left end or on the right end.
